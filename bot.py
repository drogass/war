import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from config import API_TOKEN
from handlers.main import register_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
