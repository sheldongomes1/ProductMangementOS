#!/usr/bin/env python3
"""
Slack-to-Backlog Bot

Listens for emoji reactions on Slack messages. When the trigger emoji is added,
fetches the message, synthesizes it into a backlog entry, and appends to BACKLOG.md.

Uses Socket Mode (no public URL required).

Required env vars:
    SLACK_BOT_TOKEN       - Bot User OAuth Token (xoxb-...)
    SLACK_APP_TOKEN       - App-Level Token (xapp-...) for Socket Mode
    PERSONAL_OS_PATH      - Path to personal-os repo (default: ~/AIProjects/personal-os)
    TRIGGER_EMOJI         - Emoji that triggers capture (default: brain)
    DISMISS_EMOJI         - Emoji that marks as dismissed (default: -1)
    GOOGLE_API_KEY        - Gemini API key for synthesis (optional, falls back to raw capture)
"""

import os
import sys
import json
import logging
import re
from datetime import datetime
from pathlib import Path

try:
    from slack_bolt import App
    from slack_bolt.adapter.socket_mode import SocketModeHandler
except ImportError:
    print("Missing dependency: pip install slack-bolt")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("slack-to-backlog")

PERSONAL_OS_PATH = Path(os.environ.get("PERSONAL_OS_PATH", "~/AIProjects/personal-os")).expanduser()
BACKLOG_PATH = PERSONAL_OS_PATH / "BACKLOG.md"
TRIGGER_EMOJI = os.environ.get("TRIGGER_EMOJI", "brain")
DISMISS_EMOJI = os.environ.get("DISMISS_EMOJI", "-1")

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


def get_channel_name(channel_id: str) -> str:
    try:
        resp = app.client.conversations_info(channel=channel_id)
        return resp["channel"]["name"]
    except Exception:
        return channel_id


def fetch_message(channel_id: str, message_ts: str) -> dict | None:
    try:
        resp = app.client.conversations_history(
            channel=channel_id, latest=message_ts, inclusive=True, limit=1
        )
        messages = resp.get("messages", [])
        return messages[0] if messages else None
    except Exception as e:
        logger.error(f"Failed to fetch message: {e}")
        return None


def get_user_name(user_id: str) -> str:
    try:
        resp = app.client.users_info(user=user_id)
        profile = resp["user"]["profile"]
        return profile.get("real_name") or profile.get("display_name") or user_id
    except Exception:
        return user_id


def synthesize_with_ai(text: str, channel_name: str, author: str) -> dict | None:
    """Use Gemini to synthesize the message into a structured backlog entry."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return None

    try:
        import urllib.request

        prompt = f"""You are a PM assistant. Analyze this Slack message from #{channel_name} by {author} and extract:

1. A one-line backlog item (actionable, concise, starts with a verb)
2. Category: one of [product-idea, interview-knowledge, ai-insight, competitive-intel, framework, other]
3. Why it matters for a PM targeting a Google AI role (one sentence)

Message:
{text}

Respond in JSON only:
{{"backlog_item": "...", "category": "...", "relevance": "..."}}"""

        body = json.dumps({
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.3, "maxOutputTokens": 300}
        })

        req = urllib.request.Request(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}",
            data=body.encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())

        raw = result["candidates"][0]["content"]["parts"][0]["text"]
        raw = re.sub(r"```json\s*", "", raw).replace("```", "").strip()
        return json.loads(raw)
    except Exception as e:
        logger.warning(f"AI synthesis failed, falling back to raw capture: {e}")
        return None


def append_to_backlog(entry: str):
    """Append a new entry to BACKLOG.md under a Slack Captures section."""
    if not BACKLOG_PATH.exists():
        logger.error(f"BACKLOG.md not found at {BACKLOG_PATH}")
        return False

    content = BACKLOG_PATH.read_text()
    section_header = "\n## Slack Captures\n"

    if section_header.strip() not in content:
        content += f"\n---\n{section_header}\n"

    content += entry + "\n"
    BACKLOG_PATH.write_text(content)
    logger.info("Appended to BACKLOG.md")
    return True


def post_confirmation(channel_id: str, thread_ts: str, entry_text: str):
    """Post a confirmation message in the #my-backlog channel or as a thread reply."""
    backlog_channel = os.environ.get("BACKLOG_CHANNEL")
    if backlog_channel:
        try:
            app.client.chat_postMessage(
                channel=backlog_channel,
                text=f"Captured to backlog:\n>{entry_text}"
            )
        except Exception as e:
            logger.warning(f"Failed to post to backlog channel: {e}")


@app.event("reaction_added")
def handle_reaction(event, say):
    emoji = event.get("reaction", "")
    user_id = event.get("user", "")
    item = event.get("item", {})

    if item.get("type") != "message":
        return

    channel_id = item.get("channel", "")
    message_ts = item.get("ts", "")

    if emoji == TRIGGER_EMOJI:
        logger.info(f"Trigger emoji :{TRIGGER_EMOJI}: detected in {channel_id}")

        message = fetch_message(channel_id, message_ts)
        if not message:
            logger.warning("Could not fetch message")
            return

        text = message.get("text", "").strip()
        if not text:
            return

        author = get_user_name(message.get("user", "unknown"))
        channel_name = get_channel_name(channel_id)
        today = datetime.now().strftime("%Y-%m-%d")

        synthesis = synthesize_with_ai(text, channel_name, author)

        if synthesis:
            entry = (
                f"- **[{synthesis['category']}]** {synthesis['backlog_item']}\n"
                f"  - Source: Slack #{channel_name} by {author} ({today})\n"
                f"  - Relevance: {synthesis['relevance']}"
            )
            display = synthesis["backlog_item"]
        else:
            entry = (
                f"- {text[:200]}{'...' if len(text) > 200 else ''}\n"
                f"  - Source: Slack #{channel_name} by {author} ({today})"
            )
            display = text[:100]

        if append_to_backlog(entry):
            post_confirmation(channel_id, message_ts, display)
            logger.info(f"Captured: {display}")

    elif emoji == DISMISS_EMOJI:
        logger.info(f"Dismiss emoji :{DISMISS_EMOJI}: — no action taken")


@app.event("message")
def handle_message_events(body, logger):
    pass


def main():
    token = os.environ.get("SLACK_APP_TOKEN")
    if not token:
        print("SLACK_APP_TOKEN is required for Socket Mode")
        print("See the skill's SKILL.md for setup instructions")
        sys.exit(1)

    if not os.environ.get("SLACK_BOT_TOKEN"):
        print("SLACK_BOT_TOKEN is required")
        sys.exit(1)

    logger.info(f"Starting Slack-to-Backlog bot")
    logger.info(f"Trigger emoji: :{TRIGGER_EMOJI}:")
    logger.info(f"Dismiss emoji: :{DISMISS_EMOJI}:")
    logger.info(f"Backlog path: {BACKLOG_PATH}")

    handler = SocketModeHandler(app, token)
    handler.start()


if __name__ == "__main__":
    main()
