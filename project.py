import telegram, config
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters

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
            print('In init state')
            message = update.message.text.lower()
            print(message)
            if update.message.text == "start" or update.message.text == "Привет":
                bot.send_message(update.message.from_user.id, "Привет! Введи количество желаемых рецептов")
                state = 'wait number'
            else:
                bot.send_message(update.message.from_user.id, "Я не понимаю Вас, напишите 'Привет'")
        elif state == 'wait number':
            try:
                number[update.message.from_user.id] = int(update.message.text)
                bot.send_message(update.message.from_user.id, "Введите список продуктов")
                state = 'wait products'
            except Exception as e:
                bot.send_message(update.message.from_user.id, "Пожалуйста, напишите число.")
            
        elif state == 'wait products':
            print('in wait state')

        
    
            message_text = update.message.text.lower()
            ingredients_from_list = message_text.split(', ')
            list_of_products = []
            for k,v in recipes.items():
                found = True
                for product in ingredients_from_list:
                    #print(product,v[0])
                    if product not in v[0]:
                        found = False
                        break
                if found:
                    list_of_products.append((k,v[1]))
                   
            if len(list_of_products) == 0:
                bot.send_message(update.message.from_user.id,'Рецептов не найдено! Попробуйте исключить некоторые ингредиенты')
                print('Not found for list: %s' % str(ingredients_from_list))
            i = 0
            while i < len(list_of_products) and i < number[update.message.from_user.id]:
                bot.send_message(update.message.from_user.id, list_of_products[i][0] + '. ' + list_of_products[i][1])
                i += 1
        
            bot.send_message(update.message.from_user.id, 'Если хотите продолжить, то напишите "Еще"')
            state = 'choose option'
        elif state == 'choose option':
            if update.message.text == 'Еще':
                state = 'wait number'
                bot.send_message(update.message.from_user.id, "Введите количество желаемых рецептов")
            else:
                state = 'init'
        else:
            print('ELSE')
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
