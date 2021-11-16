from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",)
    await message.answer(text=f"""Siz ushbu bot orqli har qanday matni \n Rus 👉 Uzb \n Uzb 👉 Rus \n ga osongina tarjima qilishingiz mumkin shunchaki matn yuboring!  """)