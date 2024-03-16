from aiogram import types
inline_keyword1 = types.InlineKeyboardMarkup()
buttom_1 = types.InlineKeyboardButton(text="Yes", callback_data="Yes")
buttom_2 = types.InlineKeyboardButton(text="NO", callback_data="No")
inline_keyword1.add(buttom_1, buttom_2)