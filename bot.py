from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    print("Вызван /start")
    bot.sendMessage(update.message.chat_id, text='Ну здорова, коль не шутишь!')

def talk_to_my(bot, update):
    print("Пришло сообщение: %s" %update.message.text)
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def run_bot():
    updater = Updater("269779371:AAGAKo2IhxvWeDpR2wUKSDzo_VO43BzMpyE")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_my))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()