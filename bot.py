import os
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import web

from config import Config
from route import web_server
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1002822095762

SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "@botskingdomschat")
PORT = int(Config.PORT)

class Bot(Client):
def init(self):
super().init(
"approver",
api_id=Config.API_ID,
api_hash=Config.API_HASH,
bot_token=Config.BOT_TOKEN
)
self.start_time = time.time()

async def start(self):
    await super().start()

    me = await self.get_me()
    self.mention = me.mention
    self.username = me.username
    self.uptime = Config.BOT_UPTIME

    if Config.WEBHOOK:
        runner = web.AppRunner(await web_server())
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", PORT)
        await site.start()

    print(f"{me.first_name} Is Started.....✨️")

    uptime_seconds = int(time.time() - self.start_time)
    uptime_string = str(timedelta(seconds=uptime_seconds))

    for chat_id in [Config.LOG_CHANNEL, SUPPORT_CHAT]:
        try:
            curr = datetime.now(ZoneInfo("Asia/Kolkata"))
            date = curr.strftime("%d %B, %Y")
            time_str = curr.strftime("%I:%M:%S %p")

            await self.send_photo(
                chat_id=chat_id,
                photo=Config.START_PIC,
                caption=(
                    "**I ʀᴇsᴛᴀʀᴛᴇᴅ ᴀɢᴀɪɴ!**\n\n"
                    f"ɪ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴜɴɴɪɴɢ ғᴏʀ: `{uptime_string}`\n"
                    f"📅 Date: `{date}`\n"
                    f"🕒 Time: `{time_str}`"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            "ᴜᴘᴅᴀᴛᴇs",
                            url="https://t.me/botskingdoms"
                        )
                    ]]
                )
            )

        except Exception as e:
            print(f"Failed to send message in chat {chat_id}: {e}")

if name == "main":
Bot().run()