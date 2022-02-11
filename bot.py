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
import time
import os
import logging
from telegram import BotCommand, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

from image_enhancer import imageEnhancer
#log info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = "5148449384:AAGSgPkYDmGGt-Hh1pvNv-SUkWK_YuxgfgQ"

#command handlers
#def start(update, context):
#    update.message.reply_text("Hi!")

def help(update, context):
    update.message.reply_text("Help!")

def recognize(update, context):
    update.message.reply_text("Please send your image to upscale")

def image_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download("./" + str(update.message.from_user.id) + "photo.png")
    #update.message.reply_text("What kind of upscale do you want? \n x2 \t x3 \t x4")

def text_handler(update, context):
    global enhancer
    global path
    global style
    if "Upscale" in update.message.text:
        buttons = [[KeyboardButton("x2")], [KeyboardButton("x3")], [KeyboardButton("x4")]]
        update.message.reply_text("Please choose your upscale level", reply_markup = ReplyKeyboardMarkup(buttons))
        #style = update.message.text[1]
        update.message.reply_text("Please send your image to upscale")
        path = "./" + str(update.message.from_user.id) + ".png"
    if "x2" in update.message.text or "x3" in update.message.text or "x4" in update.message.text:
        style = update.message.text


def singleMethod(update, context):
    global enhancer
    global path
    global style

    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    #path = "./" + str(update.message.from_user.id) + ".png"
    obj.download(path)
    print(f"style={style} \t path={path}")
    if style == "x2" :
        enhancer.Enhance("x2", path)
    elif style == "x3" :
        enhancer.Enhance("x3", path)
    elif style == "x4" :
        enhancer.Enhance("x4", path)
    #update.message.reply_text("What kind of upscale do you want? \n x2 \t x3 \t x4")
    if os.path.isfile(path[:len(path)-4] + "out.png"):
        update.message.reply_photo(photo=open(path[:len(path)-4] + "out.png", "rb"))
        os.remove(path)
        os.remove(path[:len(path)-4] + "out.png")



def error(update, context):
    logger.warning('Update "%d" caused error "%s"', update, context.error)

def add_commands(up : Updater):
    commands = [
        BotCommand("start", "Introduction to Bot"),
        BotCommand("help", "Gives help"),
        BotCommand("singleMethod", "Upscale your image")
    ]
    up.bot.set_my_commands(commands=commands)

def add_handlers(dp : Dispatcher):
    #commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    #dp.add_handler(CommandHandler("singleMethod", singleMethod))
    #messages
    dp.add_handler(MessageHandler(Filters.photo, singleMethod))
    #errors
    dp.add_error_handler(error)

def start(update, context):
    buttons = [[KeyboardButton("Upscale")], [KeyboardButton("Help")]]
    update.message.reply_text("Welcome", reply_markup = ReplyKeyboardMarkup(buttons))

def main():
    #updater for bot
    updater = Updater(TOKEN, use_context=True)
    
    #enhancer = imageEnhancer()
    #dispatcher
    dp = updater.dispatcher
    #add_commands(updater)
    #add_handlers(updater.dispatcher)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("recognize", recognize))
    dp.add_handler(MessageHandler(Filters.text, text_handler))
    dp.add_handler(MessageHandler(Filters.photo, singleMethod))#need to pass enhancer
    #dp.add_handler(MessageHandler(Filters.text & Filters.photo, singleMethod))#need to pass enhancer
    #log all errors
    #dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

enhancer = imageEnhancer()
path = ""
style = "x2"
if __name__ == '__main__':
    main()
