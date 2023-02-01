import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command

with open('Mikolaj.txt', 'r', encoding='utf - 8') as F:
    tok = F.read()

Bot_TOKEN = tok #токен бота

bot: Bot = Bot(Bot_TOKEN)
dp: Dispatcher = Dispatcher()

ATTEMPS: int = 7 #кількість спроб

# словник з данними користувача
user : dict = {'in_game': False,
               'secret_number': None,
               'attempts': None,
               'total_games': 0,
               'wins': 0}

#випадкове число
def get_number() -> int:
    return random.randint(1,100)

#Хендлер команди start
@dp.message(Command(commands=['start']))
async def com_start(message: Message):
    await message.answer('Даров, давай зіграєм в гру "вгадай число".\n\nЯб хотів робити більш інтелектуальні речі,'
                         'але мій господар ніфіга не може.\n\nтому маэємо шо маємо\n\nДоречі, якщо хочеш правила,'
                         'відправ команду /help\n\nНу так що, зіграємо?')

#Хендлер команди help
@dp.message(Command(commands=['help']))
async def com_help(message: Message):
    await message.answer('Я загадаю число від 1 до 100, а ти будеш його вгадувати.\nВ тебе буде 7 спроб, пілся кожної\
                         спроби я буду підказувати чи більше моє число від твого, чи меньше\n\nДоречі 7 спроб достатньо\
                          щоб ти завжди вигравав)))')

#Хендлер команди cancel
@dp.message(Command(commands=['cancel']))
async def com_cancel(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer('Добре пограли, якщо захочеш щє - пиши /start')
    else:
        await message.answer('Ми й так не граємо')

@dp.message(Text(text=['Так', 'Давай', 'Ок', 'Зіграємо', 'Yes', 'ok', 'play', 'Да'], ignore_case=True))
async def func_yes(message: Message):
    if not user['in_game']:
        await message.answer('Оу, тоды давай почнемо, я загадав число выд 1 до 100.\n\n'
                             'Спробуй вгадати.\n\n Напиши число.')
        user['in_game'] = True
        user['secret_number'] = get_number()
        user['attempts'] = ATTEMPS
    else:
        await message.answer('Йой, ми вже граємо, давай числа від 1 до 100')

@dp.message(Text(text=['Ні', 'Нє', 'No']))



if __name__ == '__main__':
    dp.run_polling(bot)




