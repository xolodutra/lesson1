from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers

def start111(bot, update):
     print("Вызван /start")
     bot.sendMessage(update.message.chat_id, text='Ну здорова, коль не шутишь!')

def talk_to_my(bot, update):
    print("Пришло сообщение: %s" % update.message.text)
    text = get_answer(update.message.text, answers)
    bot.sendMessage(update.message.chat_id, text=text)


def run_bot():
    updater = Updater("269779371:AAGAKo2IhxvWeDpR2wUKSDzo_VO43BzMpyE")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start111))
    dp.add_handler(MessageHandler([Filters.text], talk_to_my))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()