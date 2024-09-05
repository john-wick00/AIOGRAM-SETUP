import asyncio
import importlib
import os
import uvloop  # Import uvloop for better performance
from rich.console import Console
from aiogram import F
from bot.handlers import MODULES_PATH
from bot import bot, dp, router  # Import the initialized bot, dp, and router

LOG = Console()

# Enable uvloop for better performance
uvloop.install()

async def on_startup():
    LOG.print(f"[bold yellow]Loading {len(MODULES_PATH)} Modules")
    for module in MODULES_PATH:
        mod = module.replace(os.getcwd(), "")[1:].replace("/", ".").replace(".py", "")
        LOG.print(f"[bold cyan]{mod.split('.')[-1]}")
        importlib.import_module(mod)

    print("✨ Bot started")

async def main():
    # Add router to the dispatcher
    dp.include_router(router)

    await on_startup()
    await dp.start_polling(bot)

# Entry point
if __name__ == "__main__":
    asyncio.run(main())
