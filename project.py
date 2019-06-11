import telegram, config
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters

import requests
import re
from project08 import *

REQUEST_KWARGS={
    'proxy_url' : 'https://185.132.133.212:8080'
}

recipes = read_file(r'C:\Users\Анастасия\Desktop\прога\cooking_bot\receipts2.txt')
print(len(recipes))

def handle_text(bot, update):
    print('test')
    url = get_url()
    chat_id = update.message.chat_id
    if update.message.text == "start" or update.message.text == "Привет":
        bot.send_message(update.message.from_user.id, "Привет, введи список продуктов")
    else:
        bot.send_message(update.message.from_user.id, "Я не понимаю тебя, напиши 'Привет'")
    ingredients_from_list = update.message.text.split(',')
    list_of_products = []
    for element in recipes.values():
        found = True
        for product in ingredients_from_list:
            if product not in element[0]:
                found = False
                break
        if found:
            list_of_products.append(element[1])
        print(element[0], found)
        break


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
