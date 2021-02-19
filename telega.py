import telebot
import argparse

parser = argparse.ArgumentParser(description='Process message')
parser.add_argument('msg', type=str, help='messages')
args=parser.parse_args()

passw = args.msg

token = '------YourToken'
bot = telebot.TeleBot(token)



def mes_send(message):
    chat_id = '-chat_id from @get_id_bot'
    bot.send_message(chat_id, message)





if _name_ == '_main_':
    mes_send(passw)
