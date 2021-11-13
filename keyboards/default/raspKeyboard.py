from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

raspis = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⛷ Dushanba'),
            KeyboardButton(text='⛺ Seshanba'),
            KeyboardButton(text='🌁 Chorshanba'),
            KeyboardButton(text='🌃 Payshanba'),
            KeyboardButton(text='🕌 Juma'),
            KeyboardButton(text='🌄 Shanba'),
        ],
        [
            KeyboardButton(text="⬇ Boshiga"),
            KeyboardButton(text="⌨ Klaviaturani olib tashlash"),
        ],
    ],
    resize_keyboard=True
)