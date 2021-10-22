import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ThePSYREX")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/3654bea3e5284b442f932.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "NA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "incofficials")
PROJECT_NAME = getenv("PROJECT_NAME", "Psymusic R0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/PSYR3X/PsyMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
PMMSG = getenv("PMMSG", f"Hi there, This is a music assistant service of @{BOT_USERNAME}.\n\n ❗️ Rules:\n   -chatting = ignore\n   - spam = ban \n\n 👉 **this bot is the property of PSYREX , go away...**\n\n ⚠️ Disclamer: If you are sending a message here it means it is most likely going to be ignored\n    - Don t add this user to secret groups.\n   - Don t Share private info here\n\n")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
