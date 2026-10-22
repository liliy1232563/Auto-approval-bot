import os
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pyrogram.utils
from aiohttp import web
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import Config
from route import web_server

pyrogram.utils.MIN_CHANNEL_ID = -1002822095762

SUPPORT_CHAT = os.environ.get(
"SUPPORT_CHAT",
"@botskingdomschat"
)

PORT = int(Config.PORT)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "approver",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN
        )
    self.start_time = time.time()
    self.web_runner = None

async def start(self):
    # Start the HTTP server first so the platform can detect the port.
    if Config.WEBHOOK:
        try:
            app = await web_server()
            self.web_runner = web.AppRunner(app)
            await self.web_runner.setup()

            site = web.TCPSite(
                self.web_runner,
                "0.0.0.0",
                PORT
            )
            await site.start()

            print(f"Web server started on port {PORT}", flush=True)

        except Exception as e:
            print(f"Web server startup failed: {e}", flush=True)
            if self.web_runner is not None:
                await self.web_runner.cleanup()
                self.web_runner = None
            raise

    try:
        await super().start()

        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME

        print(f"{me.first_name} Is Started.....✨️", flush=True)

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
                        f"ɪ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴜɴɴɪɴɢ ғᴏʀ: "
                        f"`{uptime_string}`\n"
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
                print(
                    f"Failed to send message in chat {chat_id}: {e}",
                    flush=True
                )

    except Exception:
        if self.web_runner is not None:
            await self.web_runner.cleanup()
            self.web_runner = None
        raise

async def stop(self, *args):
    try:
        if self.web_runner is not None:
            await self.web_runner.cleanup()
            self.web_runner = None
    finally:
        await super().stop(*args)

if name == "main":
Bot().run()