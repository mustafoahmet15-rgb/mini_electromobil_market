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

@bot.message_handler(content_types=['web_app_data'])
def get_data(message): # 'message' mana shu yerda aniqlanishi shart
    try:
        # Web App'dan kelgan JSON ma'lumotni o'qiymiz
        data = json.loads(message.web_app_data.data)

        # Sana formatlash (import datetime yuqorida bo'lishi kerak)
        formatted_date = datetime.fromtimestamp(message.date).strftime('%d.%m.%Y %H:%M')

        # Buyurtma matnini shakllantiramiz
        res_text = (
            f"✅ Yangi Buyurtma qabul qilindi!\n\n"
            f"💰 Jami summa: {data['total']} $\n"
            f"👤 Mijoz: {message.from_user.first_name}\n" # '0' ni 'message.from_user.first_name' ga o'zgartiring
            f"📅 Sana: {formatted_date}"
        )

        # Foydalanuvchiga tasdiq xabarini yuboramiz
        bot.send_message(message.chat.id, res_text)

    except Exception as e:
        # Xatolik yuz bersa, shu yer ishlaydi
        bot.send_message(message.chat.id, f"⚠️ Ma'lumotni qayta ishlashda xatolik: {e}")
# Kodingizning eng oxiridagi qismni shunday o'zgartiring:
bot.infinity_polling(timeout=10, long_polling_timeout=5)
# Botni ishga tushirish (bular funksiyadan tashqarida, eng chetda turishi kerak)


while True:
    try:
        print("Bot ishga tushdi...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        time.sleep(5) # 5 soniya kutib, qayta ulanishga urinadi
