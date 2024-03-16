import os
from keybor_buttom import menu_keyword, menu_detail, category_datail, menu_1
from database import Database
import logging
from aiogram import Bot, Dispatcher, executor,  types
from dotenv import load_dotenv
from inline_keyword.post import inline_keyword1
load_dotenv()


API_TOKEN = os.getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    customer = message.from_user.username
    chat_id = str(message.chat.id)

    chek_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""  
    if len(Database.connect(chek_query, "select")) >= 1:
        print(len(Database.connect(chek_query, "select")))
        await message.answer(f"HELLO @{customer}", reply_markup= menu_keyword)
    else:
        print(f"{customer} start bot")
        query = f"""INSERT INTO users(first_name, last_name, user_name, chat_id) VALUES('{first_name}', '{last_name}', '{customer}', '{chat_id}')"""
        Database.connect(query, "insert")
        await message.answer(f"Hi @{customer}", reply_markup=menu_keyword)
        print(f"{customer}")
    

@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = str(message.chat.id)
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Hi @{data [0][3]}
        First_name: {data[0][1]}
        Last_name: {data[0][2]}""")



@dp.message_handler(lambda message: message.text == "Menyu")
async def show_menu(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Menyulardan birini tanlang:", reply_markup = menu_detail)

@dp.message_handler(lambda message: message.text == "Admin")
async def show_admin(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Siz admin bo'lishga rozimisiz?", reply_markup = inline_keyword1)

@dp.message_handler(lambda message: message.text == "Category")
async def show_category(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Categoriyalardan birini tanlang", reply_markup = category_datail)

@dp.message_handler(lambda message: message.text == "Back")
async def back(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    await messege.answer("Menyulardan birini tanlang:", reply_markup = menu_keyword)

@dp.message_handler(lambda message: message.text == "Category_1")
async def menu_01(messege: types.Message):
    # action = button_callback_menu.new(action=messege.text)
    # await messege.answer(messege.from_user.get_user_profile_photos)
    await messege.answer("Menu 1", reply_markup=menu_1) 

# @dp.message_handler(lambda message: message.text not in ["Curses", "Modules", "Pyhton"])
# async def menu_01(messege: types.Message):
#     # action = button_callback_menu.new(action=messege.text)
#     await messege.answer("Bundey bolim mavjud emas", reply_markup=menu_detail)

@dp.message_handler(commands=['send_image'])
async def send_image(message: types.Message):
    photo_url = 'https://www.freecodecamp.org/news/content/images/2021/08/chris-ried-ieic5Tq8YMk-unsplash.jpg'
    caption = 'Sizning rasmingiz'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)

@dp.callback_query_handler(lambda call: call.data == "No")
async def aggre_ref_start(query: types.CallbackQuery):
    if query.data == "No":
        await query.answer("Etiboringiz uchun raxmat")

@dp.callback_query_handler(lambda call: call.data == "Yes")
async def agre_ref_start(query: types.CallbackQuery):
    if query.data == "Yes":
        await query.answer("Siz admin sifasida botga qoshildingiz!")
        # await message.answer("/admin_command bosing")
        # db_connect()

    
@dp.message_handler(commands=['admin_command'])
async def admin_command(message: types.Message):
    query = """SELECT * FROM admins;"""
    admins = []
    for i in Database.connect(query, "select"):
        admins.append(i[1])
    if str(message.from_user.id) in admins:
        await message.reply("Salom admin")
    else:
        await message.reply("Bunday buyruq turi mavjud emas")

# @dp.message_handler()
# async def db_connect(message: types.Message):
#     customer = message.from_user.username
#     chat_id = str(message.chat.id)
#     query_str = f"""INSERT INTO admins(name, chat_id) VALUES ('{customer}', '{chat_id}');"""
#     Database.connect(query_str, "insert")
#     print(f"{customer} databasega qoshildi")
#     await message.answer("Run", reply_markup=menu_keyword)
        

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
