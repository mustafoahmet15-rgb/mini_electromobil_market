import time
import os
import telebot
import json
from telebot import types
from dotenv import load_dotenv

# .env faylidan tokenni o'qish
load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # URL ni bitta qatorga, xatosiz yozing
    web_app = types.WebAppInfo(url="https://mustafoahmet15-rgb.github.io/mini_electromobil_market/")
    
    # BU QATORLAR FUNKSIYA ICHIDA BO'LISHI SHART (Tab bosing):
    btn = types.KeyboardButton("Do'konni ochish 🛒", web_app=web_app)
    markup.add(btn)
    bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=markup)

import json
from datetime import datetime
# bot va boshqa importlar shu yerda bo'ladi...

@bot.message_handler(content_types=['web_app_data'])
def get_data(message):
    try:
        # Web App'dan kelgan JSON ma'lumotni o'qiymiz
        data = json.loads(message.web_app_data.data)

        # 1. Sana formatlash
        formatted_date = datetime.fromtimestamp(message.date).strftime('%d.%m.%Y %H:%M')

        # 2. Foydalanuvchi ismini olish
        first_name = message.from_user.first_name if message.from_user.first_name else ""
        last_name = message.from_user.last_name if message.from_user.last_name else ""
        full_name = f"{first_name} {last_name}".strip()
        
        if not full_name:
            full_name = "Mijoz"

        # 3. Buyurtma matnini shakllantiramiz
        # MUHIM: data.get() ichidagi 'product_name' Web App'dagi bilan bir xil bo'lishi kerak
        res_text = (
            f"📦 Yangi buyurtma!\n\n"
            f"👤 Foydalanuvchi: {full_name}\n"
            f"⌚ Sana: {formatted_date}\n\n"
            f"📋 Buyurtma tafsilotlari:\n"
            f"- Mahsulot: {data.get('product_name', 'Nomaʼlum')}\n"
            f"- Miqdor: {data.get('quantity', 'Nomaʼlum')}\n"
            f"- Narx: {data.get('price', 'Nomaʼlum')} UZS\n"
        )

        # Foydalanuvchiga tasdiq xabarini yuboramiz
        bot.send_message(message.chat.id, res_text)

    except Exception as e:
        # Xatolik yuz bersa, shu yer ishlaydi
        bot.send_message(message.chat.id, f"⚠️ Ma'lumotni qayta ishlashda xatolik: {e}")

# Botni ishga tushirish qismi...
# Botni ishga tushirish (bular funksiyadan tashqarida, eng chetda turishi kerak)
while True:
    try:
        print("Bot ishga tushdi...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        time.sleep(5) # 5 soniya kutib, qayta ulanishga urinadi
