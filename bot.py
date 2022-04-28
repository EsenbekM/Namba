from aiogram import executor
from config import dp
import logging
from callbacks import client_clb
from hendlers import client

client.register_handlers_client(dp)
client_clb.register_callback_handlers(dp)

# Start bot
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
