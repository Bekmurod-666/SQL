import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp,db,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name=message.from_user.full_name
    # foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.InternalError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Xush kelibsiz")
    count=db.count_users()[0]
    msg=f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvhi bor."
    await bot.send_message(chat_id=ADMINS[0],text=msg)