from telegram import Update
from telegram.ext import CallbackContext
import random

class Tirsk:
    isTirsk  = lambda self: random.random() < self.tirsk_prob
    rndTirsk = lambda self: random.choice(("tirsk", "Tirsk", "tirsk :D", "(tirsk)", "[tirsk]"))

    def __init__(self, tirsk_prob = 0.0001):
        self.tirsk_prob = tirsk_prob

    def getCommands(self):
        return dict()

    async def sendTirsk(self, update: Update, context: CallbackContext):
        chat_id = update.message.chat.id
        await context.bot.sendMessage(chat_id=chat_id, text=self.rndTirsk())

    async def messageHandler(self, update: Update, context: CallbackContext):
        if self.isTirsk():
            await self.sendTirsk(update, context)
