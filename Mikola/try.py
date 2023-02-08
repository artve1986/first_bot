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


# Обробляє команду "/stat"
@dp.message(Command(commands=['stat']))
async def process_stat_command(message: Message):
    await message.answer(f'Всьго ігор зіграно: {user["total_games"]}\n'
                         f'Виграно: {user["wins"]}')

#Хендлер команди cancel
@dp.message(Command(commands=['cancel']))
async def com_cancel(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer('Добре пограли, якщо захочеш щє - пиши /start')
    else:
        await message.answer('Ми й так не граємо')

@dp.message(Text(text=['Так', 'Давай', 'Ок', 'Зіграємо', 'Yes', 'ok', 'play', 'Да', 'передумав',
                       'згоден'], ignore_case=True))
async def func_yes(message: Message):
    if not user['in_game']:
        await message.answer('Оу, тоды давай почнемо, я загадав число выд 1 до 100.\n\n'
                             'Спробуй вгадати.\n\n Напиши число.')
        user['in_game'] = True
        user['secret_number'] = get_number()
        user['attempts'] = ATTEMPS
    else:
        await message.answer('Йой, ми вже граємо, давай числа від 1 до 100')

@dp.message(Text(text=['Ні', 'Нє', 'No', 'то'], ignore_case=True))
async def func_no(message: Message):
    if not user['in_game']:
        await message.answer('Ну як хочеш, мені воно теж нафіг треба.\n\nАле якщо передумаєш, напиши.')
    else:
        await message.answer('Агов, миж граємо, давай числа від 1 до 100\n\nАле якщо набридло грати введи'
                             'команду "/cancel"')


# Цей хендлер реагує 1 до 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def num_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Йой, да ти вгадав!!!\n\n'
                                 'Давай щє?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Моє число меньше')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Моє число більше')
            user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(f'Дідько, не лишилось спроб'
                                 f'Ти програв:(\n\nМоє число '
                                 f'було {user["secret_number"]}\n\nНу шо, '
                                 f'давай щє?')
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('Ти шо, ми щє не граємо! Хочеш?')

# Цей хендлер обробляє усі інші повідомленя
@dp.message()
async def other_text_answers(message: Message):
    if user['in_game']:
        await message.answer('Ну шо ти мені пишеш?\n\n'
                             'Давай числа від 1 до 100')
    else:
        await message.answer('Йой, легше!! Я не розумію. Давай кращє зіграємо')


if __name__ == '__main__':
    dp.run_polling(bot)




