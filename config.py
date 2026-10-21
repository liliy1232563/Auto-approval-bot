import os, time
from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    PORT = os.environ.get("PORT", "8080")
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))
    
   # Your other confgs 
    BOT_UPTIME  = time.time()
    ADMIN_URL = "https://t.me/botskingdoms"
    START_PIC   = os.environ.get("START_PIC", "https://ibb.co/DH3N4Lyr")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003842048266"))
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    FSUB_PIC = os.environ.get("FSUB_PIC", "")
    
    
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("MONGO_URI", "")

#--------------------------------------------
HELP_TXT = "<b><blockquote>Iᴀᴍ ᴀɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴀʟ ʙᴏᴛ ᴀɴᴅ ɴᴏᴛʜɪɴɢ ᴀɴʏ ᴍᴏʀᴇ ᴀɴᴅ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ ᴍʏ sᴇɴᴘᴀɪ</blockquote></b> \n\n<b><blockquote>Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴏᴜʀ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ <a href=https://t.me/botskingdoms>Seishiro</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/seishiro_atanime>Seishiro</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/seishiro_atanime>Seishiro at anime</a>\n◈ Bᴏᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+MIFq6K4VQ9tjNThl>Seishiro Bots</a>\n◈ Eɴɢ sᴜʙ/ᴅᴜʙ : <a href=https://t.me/seishiro_atanime>Seishiro at anime</a>\n◈ Hɪɴᴅɪ ᴅᴜʙ : <a href=https://t.me/seishiro_anime_is>Seishiro anime</a></blockquote></b>"
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>Bᴀᴋᴀᴀᴀ!!!....{first}\n\n<blockquote>ɪ ᴀᴍ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴀʟ ʙᴏᴛ ᴡɪᴛʜ ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ᴀɴᴅ ɪ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴘᴘʀᴏᴠᴇ ᴛʜᴇɪʀ ʀᴇǫᴜᴇsᴛs...!!.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")
#--------------------------------------------
