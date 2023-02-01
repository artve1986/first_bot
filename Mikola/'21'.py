import random

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

with open('Mikolaj.txt', 'r', encoding='utf - 8') as F:
    tok = F.read()

Bot_TOKEN = tok #токен бота

bot: Bot = Bot(Bot_TOKEN)
dp: Dispatcher = Dispatcher(bot)

deck = {
        '6♥': 6, '7♥': 7,'8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 2, 'Q♥': 3, 'K♥': 4, 'A♥': 11,
        '6♦': 6, '7♦': 7,'8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 2, 'Q♦': 3, 'K♦': 4, 'A♦': 11,
        '6♠': 6, '7♠': 7,'8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 2, 'Q♠': 3, 'K♠': 4, 'A♠': 11,
        '6♣': 6, '7♣': 7,'8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 2, 'Q♣': 3, 'K♣': 4, 'A♣': 11
        }

print(type(deck))