from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import rasp_callback



dars = {
    "⛷ Dushanba": "dushanba",
    "⛺ Seshanba": "seshanba",
    "🌁 Chorshanba": "chorshanba",
    "🌃 Payshanba":"payshanba",
    "🕌 Juma":"juma",
    "🌄 Shanba":"shanba",
}

raspMenu = InlineKeyboardMarkup(row_width=2)
for key, value in dars.items():
    raspMenu.insert(InlineKeyboardButton(text=key, callback_data=rasp_callback.new(item_name=value)))
