from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

class DoorCommandsModule:
    def __init__(self, application):
        self.application = application

    async def open_door(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        door = update.message.text
        await update.message.reply_text("Opening door: " + door)


    def add_handlers_door_commands(self):
        self.application.add_handler(CommandHandler("open_door", self.open_door))