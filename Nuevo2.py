import os
import telegram
from urllib.request import urlretrieve

# Configura el token de autenticación del bot
TOKEN = '6043283784:AAHLV11M9g3gaDj5dE-Sr5fKhSCd8CT-lOc'

# Crea un objeto de bot de Telegram
bot = telegram.Bot(token=TOKEN)

# Define una función para manejar los mensajes enviados al bot
def handle_message(update, context):
    message = update.message
    text = message.text
    
    # Si el mensaje es un enlace de descarga que contiene "mkv" o "mp4"
    if text.startswith('http') and ('.zip' in text or '.rar' in text or '.mkv' in text or '.mp4' in text):
        # Descarga el archivo desde el enlace
        file_name, headers = urlretrieve(text)
        # Envia el archivo como un documento adjunto
        message.reply_document(document=open(file_name, 'rb'))
        # Borra el archivo descargado del servidor
        os.remove(file_name)
    else:
        # Responde con un mensaje si el usuario no proporciona un enlace de descarga válido.
        message.reply_text('Por favor, proporciona un enlace de descarga válido que contenga "zip", "rar", "mkv" o "mp4".')

# Define una función para manejar los errores
def handle_error(update, context):
    error = context.error
    print(f'Error: {error}')

# Crea un objeto de despachador para registrar las funciones de manejo de mensajes y errores
dispatcher = telegram.ext.Dispatcher(bot, None)
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
dispatcher.add_error_handler(handle_error)

# Inicia el bot y espera a que lleguen nuevos mensajes
bot.polling()
