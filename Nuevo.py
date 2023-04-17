import os
import glob
from telegram import Bot
from telegram.ext import Updater

# Define la ruta de la carpeta que deseas subir
folder_path = "/content/downloads"

# Obtiene una lista de archivos en la carpeta
files = glob.glob(os.path.join(folder_path, "*"))

# Crea una instancia del bot de Telegram
bot = Bot(token="1afa55a5f3bf7058c843d1b290f79c49")

# Define el ID del chat al que deseas enviar los archivos
chat_id = "-1001536276424"

# Recorre cada archivo en la carpeta y envía el archivo al chat
for file in files:
    with open(file, "rb") as f:
        bot.send_document(chat_id=chat_id, document=f)
