from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers
from calculator import calculate
from foolmoon import fool_moon_metr
from log_bot import output_reader
import ephem

# Вот функция, которая передаёт данные в функцию log_bot
def log_writer(bot, update):
    output_log =  ['first_name', 'text' ]
    text = output_reader(update.message, output_log)
    print("что-то начало получаться?")
    bot.sendMessage(update.message.chat_id, text=text)


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

    if update.message.text in answers:
        text = get_answer(update.message.text, answers)
    else:
        text = fool_moon_metr(update.message.text)
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