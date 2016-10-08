from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers
from calculator import calculate

# Ввод команды /start в телеграм вызывает:
def start(bot, update):
     print("Вызван /start")
     bot.sendMessage(update.message.chat_id, text='Ну здорова, коль не шутишь!')

# Ввод команды /calculat вызывает :
def solver(bot, update):
    print("Кто-то хочет посчитать %s" % update.message.text)
    text = calculate(update.message.text)
    bot.sendMessage(update.message.chat_id, text=text)

# Ввод команды /count вызывает:
def count_word(bot, update):
    msg = update.message.text
    msg = len(msg.split(' ')) - 1
    text_count = 'Введено {} слов'.format(msg)
    bot.sendMessage(update.message.chat_id, text=text_count)

# Ввод слов из списка вызывает: 
def talk_to_my(bot, update):
    print("Пришло сообщение: %s" % update.message.text)
    text = get_answer(update.message.text, answers)
    bot.sendMessage(update.message.chat_id, text=text)

# Функция управления общением с ботом
def run_bot():
    updater = Updater("269779371:AAGAKo2IhxvWeDpR2wUKSDzo_VO43BzMpyE")


    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("calc", solver))
    dp.add_handler(CommandHandler("count", count_word))
    dp.add_handler(MessageHandler([Filters.text], talk_to_my))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()