import telebot
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

API_KEY = "6043283784:AAHLV11M9g3gaDj5dE-Sr5fKhSCd8CT-lOc"

bot = telebot.TeleBot(API_KEY)

# Authenticate Google Drive API
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
folder_id = '<your_folder_id_here>' # Replace with the ID of your Google Drive folder

@bot.message_handler(commands=['start'])
def start(message):
    folder = drive.CreateFile({'id': folder_id})
    folder.FetchMetadata()
    folder_url = folder['alternateLink'] # Get the shareable link
    bot.reply_to(message, "Hello, I am a Telegram bot. Here's the link to the folder: {}".format(folder_url))

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
