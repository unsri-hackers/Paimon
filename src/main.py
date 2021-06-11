from dotenv import load_dotenv
import logging
import os
from os.path import join, dirname

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO').upper())


def get_name(new_user):
    if new_user['last_name'] is None:
        user ="(" + str(new_user['first_name']) + ")"
    else:
        user ="(" + str(new_user['first_name']) + " " + str(new_user['last_name']) + ")"

    if new_user['username'] is None:
        username = ""
        if new_user['last_name'] is None:
            user =str(new_user['first_name'])
        else:
            user =str(new_user['first_name']) + " " + str(new_user['last_name'])
    else:
        username = "@" + str(new_user['username']) + " "

    return str(username) + str(user)

def welcome(update, context):
    for new_user_obj in update.message.new_chat_members:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Halo '+ get_name(new_user_obj) + '! 👋'
                                        '\n\nSelamat bergabung di grup Attack On IF, tempat berkumpulnya seluruh mahasiswa dan alumni Teknik Informatika. Feel free to drop your question about coding, tugas kuliah, skripsi, lowongan KP, atau pekerjaan di sini. Pasti dibantu jawab!'
                                        '\n\nKarena tak kenal maka tak sayang, boleh dong kenalin diri kamu sedikit. Nama, angkatan, hobi, status, instagram, twitter, github, dan lain-lain 🙈')

def send_welcome_message(update, context):
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

def intro(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Halo semuanya namaku Paimon! ^_^'
                                                                  '\nAku bakal jadi teman kalian di grup Attack On '
                                                                  'IF! Salam Kenal ya!')

if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    updater = Updater(telegram_bot_token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('intro', intro))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    dp.add_handler(MessageHandler(Filters.text, send_welcome_message))

    logging.info("🤖 Paimon is running...")
    updater.start_polling()
    updater.idle()
