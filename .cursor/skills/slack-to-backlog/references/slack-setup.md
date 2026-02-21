# Slack App Setup Guide

## 1. Create the Slack App

1. Go to https://api.slack.com/apps
2. Click **Create New App** → **From scratch**
3. Name: `PersonalOS Backlog Bot`
4. Select your workspace
5. Click **Create App**

## 2. Enable Socket Mode

1. In the app settings, go to **Socket Mode** (left sidebar)
2. Toggle **Enable Socket Mode** → ON
3. When prompted, create an App-Level Token:
   - Token name: `backlog-bot-socket`
   - Scope: `connections:write`
   - Click **Generate**
4. Copy the `xapp-...` token → save as `SLACK_APP_TOKEN`

## 3. Set Bot Permissions (OAuth & Permissions)

Go to **OAuth & Permissions** → **Scopes** → **Bot Token Scopes** and add:

| Scope | Purpose |
|-------|---------|
| `channels:history` | Read messages from public channels |
| `channels:read` | Get channel names |
| `groups:history` | Read messages from private channels |
| `groups:read` | Get private channel names |
| `reactions:read` | Detect emoji reactions |
| `users:read` | Get author names |
| `chat:write` | Post confirmation messages |

## 4. Subscribe to Events

Go to **Event Subscriptions** → Toggle ON → **Subscribe to bot events**:

| Event | Purpose |
|-------|---------|
| `reaction_added` | Trigger on emoji reactions |
| `message.channels` | Required for channel access |

Click **Save Changes**.

## 5. Install the App

1. Go to **Install App** (left sidebar)
2. Click **Install to Workspace**
3. Authorize the permissions
4. Copy the `xoxb-...` token → save as `SLACK_BOT_TOKEN`

## 6. Invite Bot to Channels

For each channel you want to monitor:
```
/invite @PersonalOS Backlog Bot
```

## 7. Configure Environment

Create `~/.slack-backlog-env` (or use your preferred method):

```bash
export SLACK_BOT_TOKEN="xoxb-your-bot-token"
export SLACK_APP_TOKEN="xapp-your-app-token"
export PERSONAL_OS_PATH="$HOME/AIProjects/product-os"
export TRIGGER_EMOJI="brain"        # React with :brain: to capture
export DISMISS_EMOJI="-1"           # React with :-1: to dismiss
export GOOGLE_API_KEY="your-key"    # Optional: for AI synthesis
export BACKLOG_CHANNEL=""           # Optional: channel ID for confirmations
```

## 8. Run the Bot

```bash
source ~/.slack-backlog-env
pip install slack-bolt
python3 ~/.cursor/skills/slack-to-backlog/scripts/slack_bot.py
```

Or run as a background service — see SKILL.md for systemd setup.
