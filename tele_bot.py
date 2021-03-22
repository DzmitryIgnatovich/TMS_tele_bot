import os
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    PrefixHandler,
    Filters
)
TOKEN = "1731265274:AAFFoLyzjWQ8Qn9M2gbkO816LYYrT8yuGHE"

HELP = """
    /start - приветствие бота
    /HELP  - это сообщение
    #run   - выполняет 
"""

def start(bot, context):
    #print(dir(context))
    #print(context.args)
    bot.message.reply_text("Hello, User")


def help(bot, context):
    bot.message.reply_text(HELP)


def run(bot, context):
    data = bot.message.text[5:]
    res = eval(data)
    bot.message.reply_text(str(res))


def message(bot, context):
    text = bot.message.text
    count = len(text)
    bot.message.reply_text(str(count))


def new(bot, context):
    data = bot.message.text[5:].split(maxsplit=1)
    file = open("./test/{}".format(data[0]), "w")
    file.write(data[1])
    file.close()


def add(bot, context):
    data = bot.message.text[6:].split(maxsplit=1)
    try:
        file = open("./test/{}".format(" " + data[0]), "a")
        file.write(data[1])
    finally:
        file.close()


def run_bot():
    bot = Updater(TOKEN, use_context=True)
    dispatcher = bot.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(PrefixHandler("#", "run", run))

    dispatcher.add_handler(PrefixHandler("^", "new", new))
    dispatcher.add_handler(PrefixHandler(">>", "add", add))

    dispatcher.add_handler(MessageHandler(Filters.text, message))


    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    run_bot()