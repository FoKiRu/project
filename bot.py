import logging
from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware  # закомментируем, если модуль не существует
from aiogram.utils import executor

# Используем предоставленный токен
API_TOKEN = '7295929162:AAENdukOQngFA83Tn5KFOEQ5fXxhK9M8nfQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())  # закомментируем, если модуль не существует

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your bot!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
