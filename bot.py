"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from image_enhancer import imageEnhancer
#log info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = "5148449384:AAGSgPkYDmGGt-Hh1pvNv-SUkWK_YuxgfgQ"


#command handlers
def start(update, context):
    update.message.reply_text("Hi!")

def help(update, context):
    update.message.reply_text("Help!")

def recognize(update, context):
    update.message.reply_text("Please send your image to upscale")

def image_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download("./input.png")
    update.message.reply_text("What kind of upscale do you want? \n x2 \t x3 \t x4")




def echo(update, context):
    enhancer = imageEnhancer()
    update.message.reply_text("I didn't understood")

    if update.message.text.lower() == "x2" :
        enhancer.Enhance("x2")
    elif update.message.text.lower() == "x3" :
        enhancer.Enhance("x3")
    elif update.message.text.lower() == "x4" :
        enhancer.Enhance("x4")

def error(update, context):
    logger.warning('Update "%d" caused error "%s"', update, context.error)

def main():
    #updater for bot
    updater = Updater(TOKEN, use_context=True)
    #enhancer = imageEnhancer()
    #dispatcher
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("recognize", recognize))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.photo, image_handler))#need to pass enhancer
    #log all errors
    dp.add_error_handler(error)
    updater.start_polling()

if __name__ == '__main__':
    main()
