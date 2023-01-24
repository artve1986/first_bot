from aiogram import Bot, Dispatcher, executor, types
with open('Mikolaj.txt', 'r', encoding='utf - 8') as F:
    tok = F.read()

TOKEN: str = tok
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)


async def process_start_command(message: types.Message):
    await message.answer('Йой, друже. Я Микола, давай побалакаєм. Краще б по пиву, але в мене нема цього/'
                         'функціоналу.')

async def process_help_command(message: types.Message):
    await message.answer('Йой, яб залюбки допоміг, але сам нічого не вмію. Тож давай побалакаєм')

async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
async def send_echo(message: types.Message):
    await message.reply(message.text)




# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_echo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)