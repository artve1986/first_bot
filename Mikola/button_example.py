from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from environs import Env

env = Env()
env.read_env()

token = env('Bot_tok')

bot: Bot = Bot(token=token)
dp: Dispatcher = Dispatcher()

#Створюєм кнопки
but_1: KeyboardButton = KeyboardButton(text='Звичайно!!')
but_2: KeyboardButton = KeyboardButton(text='Так, звісно!!')

#Створюєм об'єкт клави
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[but_1, but_2]],
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)

@dp.message(CommandStart())     #задаєм питання і вмикаєм клаву
async def start_com(message: Message):
    await message.answer(text='Хочеш пива?',
                         reply_markup=keyboard)

@dp.message(Text(text='Звичайно!!'))
async def answer_com(message: Message):
    await message.answer(text='Я теж, але я всього навсього бот :-((')

@dp.message(Text(text='Так, звісно!!'))
async def answer_com(message: Message):
    await message.answer(text='Так чого ти чекаєшь?')


if __name__ == '__main__':
    dp.run_polling(bot)