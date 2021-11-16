from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton
buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Rus--Uzb',),
            KeyboardButton(text="Uzb--Rus",),

        ],

    ],
    resize_keyboard = True
)
