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
    # GitHub manzilingizni tekshirib yozing:
    web_app = types.WebAppInfo(url="https://github.com/mustafoahmet15-rgb/mini_electromobil_market")
    btn = types.KeyboardButton("Do'konni ochish 🛒", web_app=web_app)
    markup.add(btn)
    bot.send_message(message.chat.id, "Xush kelibsiz!", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def get_data(message):
    data = json.loads(message.web_app_data.data)
    res_text = f"🛒 Yangi Buyurtma!\n\nJami summa: ${data['total']}"
    bot.send_message(message.chat.id, res_text)

print("Bot ishga tushdi...")
bot.infinity_polling()

