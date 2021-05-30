from dotenv import load_dotenv
import logging
import os
from os.path import join, dirname

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO').upper())


def welcome(update, context):
    for new_user_obj in update.message.new_chat_members:
        user = str(new_user_obj['first_name']) + " " + str(new_user_obj['last_name'])
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Halo ' + str(user) + ' ,'
                                                            '\n\nSelamat datang di grup Attack On IF! '
                                                            '\nSalam kenal yaaa!')


def intro(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Halo semuanya namaku Paimon! ^_^'
                                                                  '\nAku bakal jadi teman kalian di grup Attack On '
                                                                  'IF! Salam Kenal ya!\n\n\nEH ADA TITAN!!!')


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    updater = Updater(telegram_bot_token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('intro', intro))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    logging.info("🤖 Paimon is running...")
    updater.start_polling()
    updater.idle()
