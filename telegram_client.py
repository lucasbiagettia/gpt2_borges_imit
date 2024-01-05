from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from borges_game import BorgesGame
import os


TOKEN =  os.environ.get('BORGES_TELEGRAM_BOT_TOKEN')
borges_game = None


def start(update: Update, context: CallbackContext) -> None:
    global borges_game 
    borges_game = BorgesGame()
    update.message.reply_text('''Hola, soy un bot entrenado para imitar a Jorge Luis Borges y estás por empezar a escribir un texto conmigo:\n
    Cuando quieras terminar de escribir sólo ingresa 'fin'\n''')

def echo(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = ''
    if user_input.lower() == 'fin':
        response = "Nuestro texto quedó así: \n"
        response = response + borges_game.get_total_text()
    else:
        response = borges_game.predict(user_input)
    update.message.reply_text(response)
   
   
    

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
