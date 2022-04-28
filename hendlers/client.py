from aiogram import types, Dispatcher
from config import bot
from keyboards import language
import lists


async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           lists.hello,
                           reply_markup=language.language_markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
