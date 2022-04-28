from aiogram import types, Dispatcher
from config import bot
from keyboards import language


async def ru(call: types.CallbackQuery):
    await bot.send_message(text="Наши сервисы", chat_id=call.message.chat.id, reply_markup=language.services)


async def kg(call: types.CallbackQuery):
    await bot.send_message(text="Биздин сервистер", chat_id=call.message.chat.id, reply_markup=language.services)


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        ru,
        lambda func: func.data == "ru"
    )
    dp.register_callback_query_handler(
        kg,
        lambda func: func.data == "kg"
    )