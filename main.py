import telebot
import json

# @BotFather dan olgan tokenni shu yerga qo'ying
API_TOKEN = '8638019976:AAHWHlc50f1TJ_A84e64rLY2PqQupH1PVi0'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Xush kelibsiz! \n\nPastdagi EM_Market tugmasini bosing.")

# Mini App'dan ma'lumot kelganda
@bot.message_handler(content_types=['web_app_data'])
def get_data(message):
    # Kelgan ma'lumotni o'qiymiz
    data = json.loads(message.web_app_data.data)
    
    res_text = "🛒 Yangi Buyurtma!\n\n"
    for item in data['items']:
        res_text += f"▪️ {item['name']} — ${item['price']}\n"
    
    res_text += f"\n💰 Jami summa: ${data['total']}"
    res_text += f"\n👤 Xaridor: {message.from_user.first_name}"
    
    bot.send_message(message.chat.id, res_text, parse_mode="Markdown")

print("Bot ishga tushdi...")
bot.infinity_polling()