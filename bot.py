from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers
from calculator import calculate

def start(bot, update):
     print("Вызван /start")
     bot.sendMessage(update.message.chat_id, text='Ну здорова, коль не шутишь!')


def count_word(bot, update):
    msg = update.message.text
    msg = len(msg.split(' ')) - 1
    text_count = 'Введено {} слов'.format(msg)
    bot.sendMessage(update.message.chat_id, text=text_count)


def talk_to_my(bot, update):
    print("Пришло сообщение: %s" % update.message.text)
    user_input = update.message.text
    if '=' in user_input:
        bot.sendMessage(update.message.text, text = calculate())
    else:
        text = get_answer(update.message.text, answers)
        bot.sendMessage(update.message.chat_id, text=text)


def run_bot():
    updater = Updater("269779371:AAGAKo2IhxvWeDpR2wUKSDzo_VO43BzMpyE")


    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("calculat", talk_to_my))
    dp.add_handler(CommandHandler("count", count_word))
    dp.add_handler(MessageHandler([Filters.text], talk_to_my))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()