import os
import json

config = {
    "server": {
        "host": os.getenv("MINECRAFT_HOST", "mc.hypixel.net"),
        "port": 25565
    },
    "account": {
        "email": os.getenv("ACCOUNT_EMAIL", "")
    },
    "discord": {
        "token": os.getenv("DISCORD_TOKEN", ""),
        "channel": os.getenv("DISCORD_CHANNEL", ""),
        "allowCrosschat": [],
        "officerChannel": "",
        "allowOfficerCrosschat": [],
        "commandRole": "",
        "overrideRole": "",
        "ownerId": "",
        "prefix": os.getenv("DISCORD_PREFIX", "!"),
        "webhookURL": "",
        "officerWebhookURL": "",
        "debugWebhookURL": "",
        "serverName": "",
        "ignoreCrosschatWarning": False
    },
    "redis": {
        "host": os.getenv("REDIS_HOST", ""),
        "port": int(os.getenv("REDIS_PORT", 6379)),
        "password": os.getenv("REDIS_PASSWORD", ""),
        "clientName": "",
        "recieveChannel": "",
        "sendChannel": ""
    },
    "settings": {
        "autoaccept": False,
        "dateLimit": 30,
        "extensions": [],
        "printChat": False
    },
    "data": {
        "current_version": "",
        "latest_version": ""
    }
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
