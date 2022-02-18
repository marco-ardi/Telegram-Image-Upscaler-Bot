"""
Simple Bot to upscale images (x2, x3 or x4 upscale is currently available)

Usage:
Click on upscale, then choose your upscale level and send your image, the bot
will return the upscaled bot using image_enhancer.
"""
import os
import time
import threading
import logging
from telegram import BotCommand, KeyboardButton, ReplyKeyboardMarkup, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from image_enhancer import imageEnhancer

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = "<your token here>"


def start(update, context):
    buttons = [[KeyboardButton("🔍 Upscale")]]
    update.message.reply_text(
        "Welcome to Image Upscaler Bot!", reply_markup=ReplyKeyboardMarkup(buttons))


def help(update, context):
    update.message.reply_text(
        "Welcome to Image Upscaler Bot! \n Click on Upscale, then choose your upscale factor and send your image")


def recognize(update, context):
    update.message.reply_text("Please send your image to upscale")


def text_handler(update, context):
    global enhancer
    global path
    global style
    if "Upscale" in update.message.text:
        buttons = [[KeyboardButton("x2")], [KeyboardButton("x3")], [
            KeyboardButton("x4")]]
        update.message.reply_text(
            "Please choose your upscale level", reply_markup=ReplyKeyboardMarkup(buttons))
        # update.message.reply_text()
        path = "./" + str(update.message.from_user.id) + ".png"
    if "x2" in update.message.text or "x3" in update.message.text or "x4" in update.message.text:
        style = update.message.text
        start_buttons = [[KeyboardButton("🔍 Upscale")]]
        update.message.reply_text("Please send your image to upscale",
                                  reply_markup=ReplyKeyboardMarkup(start_buttons))


def image_handler(update, context):
    global enhancer
    global path
    global style

    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download(path)
    print(f"style={style} \t path={path}")
    update.message.reply_text("Please wait until your image is upscaled!")
    #update.message.reply_chat_action(ChatAction.TYPING, timeout=3)
    # create a thread for upscaling
    if style == "x2":
        th = threading.Thread(target=enhancer.Enhance, args=("x2", path))
        th.start()
    elif style == "x3":
        th = threading.Thread(target=enhancer.Enhance, args=("x3", path))
        th.start()
    elif style == "x4":
        th = threading.Thread(target=enhancer.Enhance, args=("x4", path))
        th.start()
    # shows "Is typing" untill the response is not ready
    while not (os.path.exists(path[:len(path)-4] + "out.png")):
        update.message.reply_chat_action(ChatAction.TYPING, timeout=5)
        time.sleep(6)

    update.message.reply_document(document=open(
        path[:len(path)-4] + "out.png", "rb"))
    os.remove(path)
    os.remove(path[:len(path)-4] + "out.png")


def error(update, context):
    logger.warning('Update "%d" caused error "%s"', update, context.error)


def add_commands(up: Updater):
    commands = [
        BotCommand("start", "Upscale your image"),
        BotCommand("help", "Gives help"),
    ]
    up.bot.set_my_commands(commands=commands)


def add_handlers(dp: Dispatcher):
    # commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # messages
    dp.add_handler(MessageHandler(Filters.text, text_handler))
    dp.add_handler(MessageHandler(
        Filters.photo | Filters.document, image_handler))
    # errors
    dp.add_error_handler(error)


def main():
    # updater for bot
    updater = Updater(TOKEN, use_context=True)
    add_commands(updater)
    add_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()


enhancer = imageEnhancer()
path = ""
style = "x2"
if __name__ == '__main__':
    main()
