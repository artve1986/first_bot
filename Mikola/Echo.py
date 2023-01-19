from aiogram import Bot, Dispatcher, executor, types
with open('Mikolaj.txt', 'r', encoding='utf - 8') as F:
    tok = F.read()

TOKEN: str = tok
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def proces_start_command(message: types.Message):
    await message.answer('Йой, друже. Я Микола, давай побалакаєм. Краще б по пиву, але в мене нема цього/'
                         'функціоналу.')

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('Йой, яб залюбки допоміг, але сам нічого не вмію. Тож давай побалакаєм')

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
@dp.message_handler()
async def send_echo(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)