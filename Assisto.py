import configparser
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters


config = configparser.ConfigParser()
config.read('config.ini')

telegramBot = Application.builder().token(config['Telegram']['BotToken']).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm Assisto!")

telegramBot.add_handler(MessageHandler(filters.TEXT, start))

telegramBot.run_polling()