from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Показать военные звания"))

def register_start_handlers(dp):
    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        await message.answer("Добро пожаловать! Я бот, который расскажет вам о военных званиях и их обязанностях. Используйте кнопки ниже.", reply_markup=main_menu)
