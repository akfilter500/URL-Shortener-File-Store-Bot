# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "16023154"))
  API_HASH = os.environ.get("API_HASH", "c216393ab439dd055858680916a3444b")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6622407174:AAFpMtGTaYjkFQlBCx-Ralt5-8cGcJAWtt4")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "File_Store_Ak_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001870553067"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "tnshort.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "7da8b3b03899edea0102565e79a412c3a977db03")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1397269319"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://pktaski502:pktaski502@cluster0.dlcz2eu.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001902923509")
  LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001740524004")
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [@AKBOTS](https://t.me/Askcaptainbot)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Askcaptainbot)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent FileStore Bot.

Join: @AKBOTS"""
