from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.raspKeyboard import raspis
from keyboards.default.startKeyboard import menuStart

from loader import dp

@dp.message_handler(Command("raspisaniya"))
async def show_rasp(message: Message):
    await message.answer("🔎 Bo'limni tanlang !", reply_markup=menuStart)

@dp.message_handler(text_contains="Admin")
async def show_admin(message: Message):
    await message.answer("🤖 Bot 🧨 @dynamitebilol tomonidan ishlab chiqildi\n"
                         "\n🧨 Boshqa proyektlar: @bilol_works")

@dp.message_handler(text_contains="Raspisaniya")
async def rasp(message: Message):
    await message.answer("🌅 Kunni tanlang !", reply_markup=raspis)


@dp.message_handler(text_contains='Dushanba')
async def dush(message: Message):
    await message.reply("Granny", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text_contains='Seshanba')
async def sesh(message: Message):
    await message.reply("Granny ", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text_contains='Chorshanba')
async def chor(message: Message):
    await message.reply("1. Rus tili\n"
                        "2. Huquq\n"
                        "3. Algebra\n"
                        "4. Ingliz tili", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text_contains='Payshanba')
async def pay(message: Message):
    await message.reply("1. Ona tili\n"
                        "2. Adabiyot\n"
                        "3. Biologiya\n"
                        "4. Informatika\n"
                        "5. Fizika",
                        reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text_contains='Juma')
async def juma(message: Message):
    await message.reply("1. Sinf soati\n"
                        "2. Algebra\n"
                        "3. Fizika\n"
                        "4. Rus tili\n"
                        "5. Jismoniy tarbiya\n"
                        "6. Geometriya", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text_contains='Shanba')
async def shanba(message: Message):
    await message.reply("1. Adabiyot\n"
                        "2. Tarbiya\n"
                        "3. Geografiya\n"
                        "4. Jahon tarixi\n"
                        "5. Biologiya\n"
                        "6. Ingliz tili",reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text_contains='Boshiga')
async def send_link(message: Message):
    await message.answer("🔎 Bo'limni tanlang !", reply_markup=menuStart)

@dp.message_handler(text_contains="Klaviatura")
async def show_menu(message: Message):
    await message.answer("⌨ Klaviatura olib tashlandi !", reply_markup=ReplyKeyboardRemove())