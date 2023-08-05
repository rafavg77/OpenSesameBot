import logging

telegram_bot_name = "OpenSesameColliBot"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d - %(funcName)s] - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logging.FileHandler("bot.log")
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(telegram_bot_name)