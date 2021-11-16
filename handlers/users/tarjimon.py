from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from googletrans import Translator
from loader import dp

translator = Translator()
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
@dp.message_handler()
async def message_javob(message: types.Message):
    til = translator.detect(message.text).lang
    print(til)

    if til == 'uz':
        await message.reply(translator.translate(message.text, src='uz',dest='ru').text)
    elif til == 'ru':
        await message.reply(translator.translate(message.text, src='ru',dest='uz').text)



    else:
        dest = 'ru'
        await message.reply(translator.translate(message.text, dest).text)