import os
from os.path import join, dirname
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def welcome(update, context):
    for new_user_obj in update.message.new_chat_members:
        user = str(new_user_obj['first_name']) + " " + str(new_user_obj['last_name'])
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Halo ' + str(user) + ' ,'
                                                            '\n\nSelamat datang di grup Attack On IF yaa! '
                                                            '\nSalam Kenal yaaa!')


def intro(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Halo semuanya namaku paimon! ^_^'
                                                                  '\nAku bakal jadi teman kalian di grup Attack On '
                                                                  'If! Salam Kenal ya!\n\n\nEH ADA TITAN!!!')


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    print(api_key)
    updater = Updater(api_key)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('intro', intro))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    updater.start_polling()
    updater.idle()
