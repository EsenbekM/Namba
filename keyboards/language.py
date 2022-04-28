from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_markup = InlineKeyboardMarkup()

ru_button = InlineKeyboardButton("RU 🇷🇺", callback_data="ru")
kg_button = InlineKeyboardButton("KG 🇰🇬", callback_data="kg")

language_markup.add(ru_button, kg_button)

services = InlineKeyboardMarkup()

namba_profi = InlineKeyboardButton("Намба профи", callback_data="namba_profi")
button_2 = InlineKeyboardButton("button 2", callback_data="1")
button_3 = InlineKeyboardButton("button 3", callback_data="2")
button_4 = InlineKeyboardButton("button 4", callback_data="3")
button_5 = InlineKeyboardButton("button 5", callback_data="4")

services.add(namba_profi, button_2, button_3, button_4, button_5)
