import time
import sys
from aiogram import Bot, Dispatcher, Router
from .config import bot_token, OWNER_ID as BOT_OWNER

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
router = Router()  # Router is now used to manage handlers
dp = Dispatcher()

StartTime = time.time()
BOT_ID: int = 0
BOT_USERNAME: str = ""
MENTION_BOT: str = ""

async def get_readable_time(seconds: int) -> str:
    time_string = ""
    if seconds < 0:
        raise ValueError("Input value must be non-negative")

    if seconds < 60:
        time_string = f"{round(seconds)}s"
    else:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        if days > 0:
            time_string += f"{round(days)} days, "
        if hours > 0:
            time_string += f"{round(hours)}h:"
        time_string += f"{round(minutes)}m:{round(seconds):02d}s"

    return time_string

async def init_bot():
    global BOT_NAME, BOT_USERNAME, BOT_ID, MENTION_BOT

    print("Connecting to the Telegram API...")
    try:
        me = await bot.get_me()
        print("Connected")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    BOT_ID = me.id
    BOT_USERNAME = me.username
    BOT_NAME = me.first_name
    MENTION_BOT = f"@{BOT_USERNAME}"

    print(
        f"Your Bot Info:\n‣ Bot ID: {BOT_ID}\n‣ Bot Name: {BOT_NAME}\n‣ Bot Username: {BOT_USERNAME}"
    )

async def main():
    await init_bot()

