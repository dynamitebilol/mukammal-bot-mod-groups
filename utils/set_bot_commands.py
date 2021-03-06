from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "π€ Botni ishga tushurish"),
            types.BotCommand("help", "π Yordam"),
            types.BotCommand("set_photo", "Guruh π· rasmini o'zgartirish"),
            types.BotCommand("set_title", "Guruh β nomini o'zgartirish "),
            types.BotCommand("set_description", "Guruh haqidagi β ma'lumotni o'zgatirish"),
            types.BotCommand("ro", "Foydalanuvchini ποΈβπ¨οΈRead-Only (RO) rejimga o'tkazish"),
            types.BotCommand("unro", " ποΈβπ¨οΈRead-Only rejimdan chiqarish"),
            types.BotCommand("ban", "π¦΅ Ban"),
            types.BotCommand("unban", "π¦΅β Bandan chiqarish"),
            types.BotCommand("raspisaniya", "π Dars jadvalini ko'rish")
        ]
    )
