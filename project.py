import telegram, config
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters
from functions import init, wait_products, wait_number, choose_option

import requests
import re
from project08 import *
PROXY_ADDR = '46.167.206.116'
PROXY_PORT = '8080'





state = 'init'



def handle_text(bot, update):
    global state
    print('test')

    try:
        print('HEY')
        #chat_id = update.message.chat_id
        if state == 'init':
            state = init(bot, update)
        elif state == 'wait products':
            state = wait_products(bot, update)
        elif state == 'wait number':
            state = wait_number(bot, update)
        elif state == 'choose option':
            state = choose_option(bot, update)
    except Exception as e:
        print('Error!!!! What: '+str(e))
        return
    
        
        
  #("No recipes found. Try adding or excluding some ingredients. I will try to help you")
    
    #result = handle_text(bot, update)

def main():
    updater = Updater(
        '762284125:AAE_wRj0y9XMNPaZ53ExUO3oKX5Ekm97riw')
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, handle_text)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
