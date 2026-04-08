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
def get_data(message):
    try:
        # Web App'dan kelgan JSON ma'lumotni o'qiymiz
        data = json.loads(message.web_app_data.data)
        
        # Buyurtma matnini shakllantiramiz
        res_text = (
            f"✅ Yangi Buyurtma qabul qilindi!\n\n"
            f"💰 Jami summa: {data['total']} $\n"
            f"👤 Mijoz: {message.from_user.first_name}\n"
            f"📅 Sana: {message.date}"
        )
        
        # Foydalanuvchiga tasdiq xabarini yuboramiz
        bot.send_message(message.chat.id, res_text, parse_mode="Markdown")
        
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Ma'lumotni qayta ishlashda xatolik yuz berdi.")

print("Bot ishga tushdi...")
bot.infinity_polling()

