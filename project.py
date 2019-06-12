import telegram, config
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters
from functions import init, wait_products, wait_number, choose_option

import requests
import re
from project08 import *

PROXY_ADDR = '191.242.230.135'
PROXY_PORT = '8080'

REQUEST_KWARGS={
    #'proxy_url' : 'https://185.132.133.212:8080'
    'proxy_url' : 'https://%s:%s' % (PROXY_ADDR,PROXY_PORT)
}

recipes = read_file(r'C:\Users\Анастасия\Desktop\прога\RecipesBot\receipts2.txt')
print(len(recipes))
state = 'init'
number = {}


def handle_text(bot, update):
    global state
    print('test')

    try:
        print('HEY')
        #chat_id = update.message.chat_id
        if state == 'init':
            init()
        elif state == 'wait_products':
            wait_products()
        elif state == 'wait number':
            wait_number()
        elif state == 'choose option':
            
    except Exception as e:
        print('Error!!!! What: '+str(e))
        return
        
        
  #("No recipes found. Try adding or excluding some ingredients. I will try to help you")
    
    #result = handle_text(bot, update)

def main():
    updater = Updater(
        '762284125:AAE_wRj0y9XMNPaZ53ExUO3oKX5Ekm97riw',
        request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, handle_text)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
