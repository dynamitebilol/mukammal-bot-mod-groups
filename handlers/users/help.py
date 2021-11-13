from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - 🤖 Botni ishga tushirish",
            "/help - 📜 Yordam\n"
            "/raspisaniya - 📄 Dars jadvalini 👁️‍🗨️ ko'rish")
    
    await message.answer("\n".join(text))