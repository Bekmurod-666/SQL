from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.dispatcher import Command

from loader import dp, db


@dp.message_handler(Command("year"))
async def send_year(message: types.Message, state: FSMContext):
    await message.answer("Yoshingizni kiriting")
    await state.set_state("year")


@dp.message_handler(state="year")
async def send_year(message: types.Message, state: FSMContext):
    years = message.text
    db.update_user_year(year=years, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Baza yangilandi: {user}")
    await state.finish()
