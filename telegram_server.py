import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

from borges_game import BorgesGame



borges_game = None
TOKEN =  os.environ.get('BORGES_TELEGRAM_BOT_TOKEN')


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: CallbackContext) -> None:
    global borges_game 
    borges_game = BorgesGame()
    await update.message.reply_text('''Hola, soy un bot entrenado para imitar a Jorge Luis Borges y estás por empezar a escribir un texto conmigo:\nCuando quieras terminar de escribir sólo ingresa 'fin'\n''')



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
    response = ''
    if user_input.lower() == 'fin':
        response = "Nuestro texto quedó así: \n"
        response = response + borges_game.get_total_text()
    else:
        response = borges_game.predict(user_input)
    await update.message.reply_text(response)


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()