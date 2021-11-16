from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

onatili_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Rus tili',callback_data='ru'),
            InlineKeyboardButton(text="O'zbek tili",callback_data= 'uz'),

        ],


    ],
    resize_keyboard = True
)
