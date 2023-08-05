#!/usr/bin/env python
from utils.logger_config import logger, logging, telegram_bot_name
from config.config import load_config

from telegram import __version__ as TG_VER
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import Update
from telegram.ext import Application
from modules.initial_commands_module import InitialCommandsModule
from modules.door_commands_module import DoorCommandsModule

logger = logging.getLogger(telegram_bot_name)
config = load_config()

def main():
    application = Application.builder().token(config["telegram_token"]).build()

    initial_commands_module = InitialCommandsModule(application)
    initial_commands_module.add_handlers_initial_commands()

    door_commands_module = DoorCommandsModule(application)
    door_commands_module.add_handlers_door_commands()

    application.run_polling(allowed_updates=Update.ALL_TYPES)
    logger.info("Bot Started!!")


if __name__ == '__main__':
    main()