from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default.startKeyboard import menuStart
from keyboards.inline.raspisaniyaKeyboard import raspMenu

from loader import dp

@dp.message_handler(Command("raspisaniya"))
async def show_rasp(message: Message):
    await message.answer("๐ Bo'limni tanlang !", reply_markup=menuStart)

@dp.message_handler(text_contains="Admin")
async def show_admin(message: Message):
    await message.answer("๐ค Bot ๐งจ @dynamitebilol tomonidan ishlab chiqildi\n"
                         "\n๐งจ Boshqa proyektlar: @bilol_works")

@dp.message_handler(text_contains="Raspisaniya")
async def rasp(message: Message):
    await message.answer("๐ Kunni tanlang !", reply_markup=raspMenu)


@dp.callback_query_handler(text_contains='dushanba')
async def dush(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("โท Dushanba\n"
                              "\n1. Kimyo\n"
                              "2. Jahon.Tarix\n"
                              "3. CHQBT\n"
                              "4. Jismoniy Tarbiya\n"
                              "5. Fizika\n")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='seshanba')
async def sesh(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("โบ Seshanba\n"
                            "\n1. Algebra\n"
                              "2. Geometriya\n"
                              "3. Ingliz tili\n"
                              "4. Kimyo\n"
                              "5. Informatika\n"
                              "6. Fizika")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='chorshanba')
async def chor(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("๐ Chorshanba\n"
                        "\n1. Rus tili\n"
                        "2. Geometriya\n"
                        "3. Algebra\n"
                        "4. Ona tili\n"
                        "5. Huquq\n"    
                        "6. Ingliz tili")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='payshanba')
async def pay(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("๐ Payshanba\n"
                        "\n1. Ona tili\n"
                        "2. Adabiyot\n"
                        "3. Biologiya")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='juma')
async def juma(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("๐ Juma\n"
                        "\n1. Sinf soati\n"
                        "2. Algebra\n"
                        "3. Biologiya\n"
                        "4. Rus tili\n"
                        "5. Jismoniy tarbiya")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='shanba')
async def shanba(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("๐ Shanba \n"
                        "\n1. Adabiyot\n"
                        "2. Tarbiya\n"
                        "3. Ingliz tili\n"
                        "4. O'zb. tarixi\n"
                        "5. Geografiya\n"
                        "6. Informatika")
    await call.answer(cache_time=60)

@dp.message_handler(text_contains='Boshiga')
async def send_link(message: Message):
    await message.answer("๐ Bo'limni tanlang !", reply_markup=menuStart)

@dp.message_handler(text_contains="Klaviatura")
async def show_menu(message: Message):
    await message.answer("โจ Klaviatura olib tashlandi !", reply_markup=ReplyKeyboardRemove())
