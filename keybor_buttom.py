from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database import Database

menu_keyword= ReplyKeyboardMarkup([
    [KeyboardButton("Menyu"), KeyboardButton("Admin"),
     KeyboardButton("Category")]
    ], resize_keyboard=True)

menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM menu;"
for i in Database.connect(query, "select"):
    menu_detail.add(KeyboardButton(i[1]))
menu_detail.add(KeyboardButton("Back"))

category_datail = ReplyKeyboardMarkup([
    [KeyboardButton("Category_1")],
    [KeyboardButton("Category_1")],
    [KeyboardButton("Category_1")],
    [KeyboardButton("Category_1")],
    [KeyboardButton("Category_1")],
], resize_keyboard=True)

menu_1 = ReplyKeyboardMarkup([
    [KeyboardButton("Back")],
    [KeyboardButton("Back")],
    [KeyboardButton("Back")],
], resize_keyboard=True)