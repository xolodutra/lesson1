from telegram.ext import Updater

def run_bot():
    updater = Updater("269779371:AAGAKo2IhxvWeDpR2wUKSDzo_VO43BzMpyE")
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()