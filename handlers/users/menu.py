from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default.startKeyboard import menuStart
from keyboards.inline.raspisaniyaKeyboard import raspMenu

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
    await message.answer("🌅 Kunni tanlang !", reply_markup=raspMenu)


@dp.callback_query_handler(text_contains='dushanba')
async def dush(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("⛷ Dushanba\n"
                              "\n1. Ona tili\n"
                              "2. Fizika\n"
                              "3. Biologiya\n"
                              "4. Adabiyot\n"
                              "5. Ingliz tili\n")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='seshanba')
async def sesh(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("⛺ Seshanba\n"
                            "\n1. Kimyo\n"
                              "2. CHQBT\n"
                              "3. Algebra\n"
                              "4. Ingliz tili\n"
                              "5. Tadbirkorlik\n")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='chorshanba')
async def chor(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("🌁 Chorshanba\n"
                        "\n1. Ingliz tili\n"
                        "2. Huquq\n"
                        "3. Astronomiya\n"
                        "4. Geometriya\n"
                        "5. Informatika\n"    
                        "6. Rus tili\n"
                        "7. Jismoniy")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='payshanba')
async def pay(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("🌃 Payshanba\n"
                        "\n1. Informatika\n"
                        "2. Ona tili\n"
                        "3. Kimyo\n"
                        "4. Rus tili\n"
                        "5. Jismoniy")
                        


    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='juma')
async def juma(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("🕌 Juma\n"
                        "\n1. Sinf soati\n"
                        "2. Algebra\n"
                        "3. Fizika\n"
                        "4. Jahon Tarixi\n"
                        "5. Geometriya\n"
                        "6. Tarbiya")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='shanba')
async def shanba(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("🌄 Shanba \n"
                        "\n1. Adabiyot\n"
                        "2. Biologiya\n"
                        "3. O'zb. tarixi\n"
                        "4. Algebra\n")
                        

    await call.answer(cache_time=60)

@dp.message_handler(text_contains='Boshiga')
async def send_link(message: Message):
    await message.answer("🔎 Bo'limni tanlang !", reply_markup=menuStart)

@dp.message_handler(text_contains="Klaviatura")
async def show_menu(message: Message):
    await message.answer("⌨ Klaviatura olib tashlandi !", reply_markup=ReplyKeyboardRemove())
