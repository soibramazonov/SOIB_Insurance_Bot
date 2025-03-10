import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# Bot va dispatcher yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Klaviatura tugmalari
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("📑 Sug'urta qilish"))
menu.add(KeyboardButton("☎ Operator bilan bog'lanish"))

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Assalomu alaykum! Sug‘urta botiga xush kelibsiz.
Quyidagi menyudan tanlang:", reply_markup=menu)

@dp.message_handler(Text(equals="📑 Sug'urta qilish"))
async def insurance_service(message: types.Message):
    await message.answer("Iltimos, tex pasportdagi mashina raqamini kiriting (masalan, 01A123BD):")

@dp.message_handler(Text(equals="☎ Operator bilan bog'lanish"))
async def contact_operator(message: types.Message):
    await bot.send_message(chat_id=ADMIN_ID, text=f"📞 Operatorga ulanish talabi!
👤 Foydalanuvchi: {message.from_user.full_name}
🆔 ID: {message.from_user.id}")
    await message.answer("Operator bilan bog'lanish talabi yuborildi! Tez orada siz bilan bog‘lanamiz.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
