from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(commands='yordam')
async def bot_yordam(message: types.Message):
    await message.answer(f"Yordam keremi, {message.from_user.full_name}?")