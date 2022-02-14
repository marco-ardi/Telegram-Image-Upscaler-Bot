"""
Simple Bot to upscale images (x2, x3 or x4 upscale is currently available)

Usage:
Click on upscale, then choose your upscale level and send your image, the bot
will return the upscaled bot using image_enhancer.
"""
import os
import logging
from telegram import BotCommand, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from image_enhancer import imageEnhancer
# log info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = "5148449384:AAGSgPkYDmGGt-Hh1pvNv-SUkWK_YuxgfgQ"


def start(update, context):
    buttons = [[KeyboardButton("Upscale")], [KeyboardButton("Help")]]
    update.message.reply_text(
        "Welcome", reply_markup=ReplyKeyboardMarkup(buttons))


def help(update, context):
    update.message.reply_text(
        "Welcome to Image Upscaler Bot! \n Click on Upscale, then choose your upscale factor and send your image")


def recognize(update, context):
    update.message.reply_text("Please send your image to upscale")


def image_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download("./" + str(update.message.from_user.id) + "photo.png")


def text_handler(update, context):
    global enhancer
    global path
    global style
    if "Upscale" in update.message.text:
        buttons = [[KeyboardButton("x2")], [KeyboardButton("x3")], [
            KeyboardButton("x4")]]
        update.message.reply_text(
            "Please choose your upscale level", reply_markup=ReplyKeyboardMarkup(buttons))
        #update.message.reply_text()
        path = "./" + str(update.message.from_user.id) + ".png"
    if "x2" in update.message.text or "x3" in update.message.text or "x4" in update.message.text:
        style = update.message.text
        start_buttons = [[KeyboardButton("Upscale")], [KeyboardButton("Help")]]
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
    if style == "x2":
        enhancer.Enhance("x2", path)
    elif style == "x3":
        enhancer.Enhance("x3", path)
    elif style == "x4":
        enhancer.Enhance("x4", path)
    if os.path.isfile(path[:len(path)-4] + "out.png"):
        #this would compress the output image, so we sent it as a document instead
        #update.message.reply_photo(photo=open(
        #    path[:len(path)-4] + "out.png", "rb"))
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
    dp.add_handler(MessageHandler(Filters.photo, image_handler))
    # errors
    dp.add_error_handler(error)


def main():
    # updater for bot
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    add_commands(updater)
    add_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()


enhancer = imageEnhancer()
path = ""
style = "x2"
if __name__ == '__main__':
    main()
