from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers

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
    if '=' in text:
        bot.sendMessage(update.message.chat_id)
    else:
        text = get_answer(update.message.text, answers)
        bot.sendMessage(update.message.chat_id, text=text)

# def talk_to_me(bot, update):
#    print("Пришло сообщение: " + update.message.text)
#    user_text = update.message.text
#    if "=" in user_text:
#        bot.sendMessage(update.message.chat_id, text = solver(user_text))
#    else:    
#        bot.sendMessage(update.message.chat_id, text = answer.answer(user_text))

def run_bot():
    updater = Updater("269779371:AAGAKo2IhxvWeDpR2wUKSDzo_VO43BzMpyE")


    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("calculat", calculat))
    dp.add_handler(CommandHandler("count", count_word))
    dp.add_handler(MessageHandler([Filters.text], talk_to_my))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()