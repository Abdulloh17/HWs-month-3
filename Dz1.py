import re
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("""
        Привет это BOT_Dz
        он поожет вам с домашками.
        Выберите предмет:
        - Алгебра 
        - Русский язык
        - Английский язык
        - Биология
        """)


def bot_info(update: Update, context: CallbackContext):
    update.message.reply_text("""
        Привет! Это бот поможет тебе с домашками и не получить двойки.
        Работаем 10 лет!
        Удачи в учебе! 
        """)

def get_greeteng_filter(greeting: str):
    return Filters.regex(re.compile(f"^{greeting}$", re.IGNORECASE)) & Filters.update.message


def reply_greeteng(update: Update, context: CallbackContext):
    update.message.reply_text('Привет, как дела в школе?')

def copy_text(update: Update, context: CallbackContext):
    update.message.reply_text(f'{update.message.text}')

def main():
    updater = Updater("5708132124:AAHmSaF53b8JpMIdYCJ6gR9cgwvyQxUZgss")
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(CommandHandler("about", bot_info))
    updater.dispatcher.add_handler(MessageHandler(get_greeteng_filter('Привет'), reply_greeteng))
    updater.dispatcher.add_handler(MessageHandler(Filters.update.message & Filters.text, copy_text))
    updater.start_polling()
    print('Started')
    updater.idle()

if __name__ == "__main__":
    main()