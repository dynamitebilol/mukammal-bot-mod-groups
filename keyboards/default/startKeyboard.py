from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📄 Raspisaniya'),
            KeyboardButton(text='👨‍💻 Admin'),
            KeyboardButton(text="⌨ Klaviaturani olib tashlash"),
        ],
    ],
    resize_keyboard=True
)