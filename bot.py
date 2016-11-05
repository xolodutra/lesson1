# Если кто-то когда-то будет читать это, знайте, это мой первый самостоятельный (почти)
# код. Поэтому мусор из горы комментариев нужен, чтобы понимать как всёэто работает. 
# Клянусь, когда буду программистом, не буду так мусорить.


# Импортировали бота
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Импортируем внешние функции
from answers import get_answer, answers
from calculator import calculate
from foolmoon import fool_moon_metr
from log_bot import output_reader

# Импортируем библиотеки
import ephem
import csv
from datetime import datetime
import os

# Эта функция собирает данные из выдачи телеграма и 
# просто записывает их построчно в текстовый файл
def log_writer(from_user, to_user, username):
    return output_reader(from_user, to_user, username)


# Эта функция собирает из выдачи телеграма 
def csv_writer(telegram_out):
    # print(telegram_out, datetime.now())
    user_info = {
        'content': telegram_out.text,
        'date': datetime.now().strftime('%d.%m.%Y'),
        'time': datetime.now().strftime('%H:%M'),
        'username': telegram_out.chat.username,
    }

    with open('export.csv', 'a', encoding='utf-8') as f:
        fields = ['date', 'time', 'username', 'content']
        writer = csv.DictWriter(f, fields, delimiter=';')
        log_size = os.path.getsize('export.csv')
        if log_size == 0:
            writer.writeheader()
        writer.writerow(user_info)


# Ввод команды /start в телеграм вызывает:
def start(bot, update):
    from_user = "Вызван /start"
    to_user = "Ну здорова, коль не шутишь!😄"
    print(from_user)
    bot.sendMessage(update.message.chat_id, text=to_user)
    log_writer(from_user, to_user, update.message.chat.username)
    try:
        csv_writer(update.message)
    except Exception as e:
        print(e)



# Ввод команды /calculat вызывает :
def solver(bot, update):
    print("Кто-то хочет посчитать %s" % update.message.text)
    text = calculate(update.message.text)
    bot.sendMessage(update.message.chat_id, text=text)
    csv_writer(update.message)

# Ввод команды /count вызывает:
def count_word(bot, update):
    msg = update.message.text
    msg = len(msg.split(' ')) - 1
    text_count = 'Введено {} слов'.format(msg)
    bot.sendMessage(update.message.chat_id, text=text_count)
    csv_writer(update.message)
    try:
        log_writer(msg, text_count, update.message.chat.username)
    except Exception as e:
        print(e)

# Ввод слов из списка вызывает: 
def talk_to_my(bot, update):
    print("Пришло сообщение: %s" % update.message.text)
    if update.message.text in answers:
        text = get_answer(update.message.text, answers)
        log_writer(update.message.text, text ,update.message.chat.username)
    else:
        text = fool_moon_metr(update.message.text)
        log_writer(update.message.text, text ,update.message.chat.username)
    bot.sendMessage(update.message.chat_id, text=text)
    csv_writer(update.message)

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