from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.dispatcher import Command

from loader import dp, db


@dp.message_handler(Command("email"))
async def send_email(message: types.Message, state: FSMContext):
    await message.answer("Email manzilingizni yuboring")
    await state.set_state("email")

@dp.message_handler(state="email")
async def send_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_user_email(email=email, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Baza yangilandi: {user}")
    await state.finish()