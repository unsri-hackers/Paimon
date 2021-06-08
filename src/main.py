from dotenv import load_dotenv
import logging
import os
from os.path import join, dirname

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO').upper())


def welcome(update, context):
    for new_user_obj in update.message.new_chat_members:
        if( new_user_obj['last_name'] is None):
            user = str(new_user_obj['first_name'])
        else:
            user ="(" + str(new_user_obj['first_name']) + " " + str(new_user_obj['last_name']) + ")"

        if( new_user_obj['username'] is None):
            username = ""
        else:
            username = "@" + str(new_user_obj['username']) + " "
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Halo '+ str(username) + str(user) + ' ,'
                                                            '\n\nSelamat datang di grup Attack On IF! '
                                                            '\nSalam kenal yaaa!')
def echo(update, context):
    cid = update.message.chat.id 
    message_text = update.message.text 
    user_id = update.message.from_user.id 
    user_name = update.message.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"

    words = message_text.split(" ")

    for i in range(len(words)):
        str_temp = "" 

        # get Unique Character
        arr_temp=[]
        for char in words[i]:
            if char not in arr_temp:
                arr_temp.append(char)

        # List to String
        message_text_temp = str_temp.join(arr_temp)

        words[i] = message_text_temp.replace(".","")
        words[i] = words[i].replace("!","")
        words[i] = words[i].lower()

    if "hi" in words:
        context.bot.send_message(cid,"Hii, " + mention,parse_mode="Markdown")
    elif "halo" in words:
        context.bot.send_message(cid,"Haloo, " + mention,parse_mode="Markdown")
    elif "hai" in words:
        context.bot.send_message(cid,"Haii, " + mention,parse_mode="Markdown")
    elif "helo" in words:
        context.bot.send_message(cid,"Heloo, " + mention,parse_mode="Markdown")

def echo_message(message):
    cid = message.chat.id 
    message_text = message.text 
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"

    if message_text.lower() == "hi":
        bot.send_message(cid,"Hi, " + mention,parse_mode="Markdown")

def intro(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Halo semuanya namaku Paimon! ^_^'
                                                                  '\nAku bakal jadi teman kalian di grup Attack On '
                                                                  'IF! Salam Kenal ya!\n\n\nEH ADA TITAN!!!')
def tes(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='tes Running bot')


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    updater = Updater(telegram_bot_token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('intro', intro))
    dp.add_handler(CommandHandler('tes', tes))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    logging.info("🤖 Paimon is running...")
    updater.start_polling()
    updater.idle()
