---
name: slack-to-backlog
description: Capture ideas from Slack channels into the PersonalOS backlog via emoji reactions. Use when the user wants to (1) set up the Slack-to-backlog bot, (2) connect Slack channels to their backlog, (3) configure emoji triggers for idea capture, (4) troubleshoot the Slack bot, (5) process or review Slack captures in BACKLOG.md, or (6) asks about the Slack integration workflow.
---

# Slack-to-Backlog

Capture product ideas, interview knowledge, and AI insights from Slack channels into BACKLOG.md with a single emoji reaction.

## How It Works

1. You read a message in any Slack channel the bot is in
2. React with :brain: (or configured trigger emoji) to capture it
3. Bot fetches the message, synthesizes it via Gemini into a structured entry
4. Entry is appended to `BACKLOG.md` under `## Slack Captures` with source attribution
5. React with :-1: to dismiss (no action taken)

## Setup

For first-time setup, follow [references/slack-setup.md](references/slack-setup.md). Summary:

1. Create a Slack app at https://api.slack.com/apps with Socket Mode enabled
2. Add bot scopes: `channels:history`, `channels:read`, `groups:history`, `groups:read`, `reactions:read`, `users:read`, `chat:write`
3. Subscribe to events: `reaction_added`, `message.channels`
4. Install to workspace, invite bot to target channels
5. Set env vars: `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, `PERSONAL_OS_PATH`
6. Optional: set `GOOGLE_API_KEY` for AI-powered synthesis, `TRIGGER_EMOJI` to customize

## Running the Bot

Install dependency and start:

```bash
pip install slack-bolt
source ~/.slack-backlog-env
python3 scripts/slack_bot.py
```

### Run as Background Service (systemd)

Create `/etc/systemd/user/slack-backlog.service`:

```ini
[Unit]
Description=Slack-to-Backlog Bot
After=network.target

[Service]
EnvironmentFile=%h/.slack-backlog-env
ExecStart=/usr/bin/python3 %h/AIProjects/personal-os/.cursor/skills/slack-to-backlog/scripts/slack_bot.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

Enable and start:
```bash
systemctl --user daemon-reload
systemctl --user enable slack-backlog
systemctl --user start slack-backlog
journalctl --user -u slack-backlog -f
```

## Backlog Entry Format

With AI synthesis (Gemini available):

```markdown
- **[product-idea]** Build a tool that evaluates AI features against responsible AI principles
  - Source: Slack #ai-product-sense by Jane Smith (2026-02-18)
  - Relevance: Directly maps to Google's responsible AI framework and interview dimensions
```

Without AI synthesis (raw capture):

```markdown
- Interesting thread about how Google evaluates AI product launches internally...
  - Source: Slack #pm-community by John Doe (2026-02-18)
```

## Configuration

| Env Var | Default | Purpose |
|---------|---------|---------|
| `SLACK_BOT_TOKEN` | required | Bot User OAuth Token (`xoxb-...`) |
| `SLACK_APP_TOKEN` | required | App-Level Token for Socket Mode (`xapp-...`) |
| `PERSONAL_OS_PATH` | `~/AIProjects/personal-os` | Path to the PersonalOS repo |
| `TRIGGER_EMOJI` | `brain` | Emoji that triggers capture (:brain:) |
| `DISMISS_EMOJI` | `-1` | Emoji that dismisses (:-1:) |
| `GOOGLE_API_KEY` | optional | Gemini API key for intelligent synthesis |
| `BACKLOG_CHANNEL` | optional | Channel ID where confirmations are posted |

## Processing Captured Items

After items accumulate in `## Slack Captures`, process them with the standard backlog flow:

1. Say "clear my backlog" or "process backlog" to the agent
2. AGENTS.md takes over: deduplication, goal-checking, task creation
3. Each item gets evaluated against GOALS.md for relevance

## Synthesis Details

When `GOOGLE_API_KEY` is set, the bot uses Gemini to classify each message into:

| Category | Captures |
|----------|----------|
| `product-idea` | New mini-product or feature ideas |
| `interview-knowledge` | PM frameworks, case studies for Google interviews |
| `ai-insight` | Technical AI learnings relevant to PM work |
| `competitive-intel` | Product moves by Google, competitors, AI ecosystem |
| `framework` | Mental models, decision-making patterns |

For full prompt details and customization, see [references/synthesis-prompt.md](references/synthesis-prompt.md).

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Bot doesn't react to emoji | Ensure `reaction_added` event subscription is active and bot is invited to the channel |
| "Missing dependency" error | Run `pip install slack-bolt` |
| Message fetch fails | Check `channels:history` / `groups:history` scope |
| Synthesis returns raw text | Verify `GOOGLE_API_KEY` is set and valid |
| BACKLOG.md not found | Check `PERSONAL_OS_PATH` points to the correct repo |
| Socket connection drops | Bot auto-reconnects; check `systemctl --user status slack-backlog` |
