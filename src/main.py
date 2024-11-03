import telebot

import requests

TOKEN = "your token"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hey my friend, welcome to the bot. Can I help you?")

@bot.message_handler(func=lambda m: True)
def show_price_btcusdt(message):
    symbol = message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if response.status_code == 200:
        data = response.json()
        bot.reply_to(message, f"{symbol} price is : {data['price']}")
    else:
        bot.reply_to(message, "You have made a typo in your request. Please correct it.")

bot.infinity_polling()
