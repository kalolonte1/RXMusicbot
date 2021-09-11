import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "KGSUPERBOT")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/0f6f8a8a5ad69fe5ecf3d.png")
BOT_IMG = getenv("BOT_IMAGE", "https://telegra.ph/file/07293ccbffed8887f1f71.jpg") 
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/07293ccbffed8887f1f71.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "KenzxMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kennedyassistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "zeusnihprend") 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "rxsupportch") 
OWNER_NAME = getenv("OWNER_NAME", "shutupbitchesss") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "knsgnwn") 
PMPERMIT = getenv("PMPERMIT", "ENABLE")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
