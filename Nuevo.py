import telebot
import os

API_KEY = "6043283784:AAHLV11M9g3gaDj5dE-Sr5fKhSCd8CT-lOc"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    # Define the folder path to send
    folder_path = "/content/downloads1"

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Send the folder to the user
        bot.send_document(message.chat.id, open(folder_path, 'rb'))
    else:
        bot.reply_to(message, "The folder does not exist.")

    bot.reply_to(message, "Hello, I am a Telegram bot. Use /help to see what I can do.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start \n /info \n /help \n /status")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I am a simple Telegram bot created using the python-telegram-bot library.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I am up and running.")
    
print("Hey, I am up....")
bot.polling()
