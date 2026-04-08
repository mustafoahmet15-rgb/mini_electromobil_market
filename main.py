import json
import os
import time
import telebot
from telebot import types
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo(url="https://mustafoahmet15-rgb.github.io/mini_electromobil_market/")
    btn = types.KeyboardButton("Do'konni ochish 🛒", web_app=web_app)
    markup.add(btn)
    bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def get_data(message):
    try:
        data = json.loads(message.web_app_data.data)
        
        # 1. Sana formatlash (rasmdagi 177... raqamni chiroyli sanaga aylantiradi)
        formatted_date = datetime.fromtimestamp(message.date).strftime('%d.%m.%Y %H:%M')

        # 2. Foydalanuvchi ismini olish
        user = message.from_user
        full_name = f"{user.first_name} {user.last_name if user.last_name else ''}".strip()
        if not full_name:
            full_name = "Mijoz"

        # 3. Savatdagi barcha mahsulotlarni matnga aylantirish
        items_text = ""
        for item in data.get('items', []):
            items_text += f"🔹 {item.get('name')}: {item.get('price')} UZS\n"

        # 4. Yakuniy xabarni shakllantirish
        res_text = (
            f"✅ Yangi buyurtma qabul qilindi!\n\n"
            f"👤 Mijoz: {full_name}\n"
            f"📅 Sana: {formatted_date}\n\n"
            f"📋 Buyurtma tarkibi:\n"
            f"{items_text}\n"
            f"💰 Jami summa: {data.get('total', 0)} UZS"
        )

        bot.send_message(message.chat.id, res_text, parse_mode="Markdown")

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Xatolik: {e}")

# Botni uzluksiz ishlatish (infinity_polling terminaldagi xatolarni kamaytiradi)
if __name__  == "__main__":
    while True:
        try:
            print("Bot ishga tushdi...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            time.sleep(5)
