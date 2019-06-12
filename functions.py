import telegram, config
from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler,Filters


import requests
import re
from project08 import *

number = {}
recipes = read_file(r'C:\Users\Анастасия\Desktop\прога\RecipesBot\receipts2.txt')
print(len(recipes))

def init(bot, update):
    if update.message.text == "start" or update.message.text == "Привет":
        bot.send_message(update.message.from_user.id, "Привет! Введите количество рецептов")
        state = 'wait number'
        return state
    else:
        bot.send_message(update.message.from_user.id, "Я не понимаю Вас, напишите 'Привет'")
    pass


def wait_products(bot, update):
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
    while i < len(list_of_products) and i < 5:
        bot.send_message(update.message.from_user.id, list_of_products[i][0] + '. ' + list_of_products[i][1])
        i += 1
    bot.send_message(update.message.from_user.id, 'Если хотите продолжить, то напишите "Еще"')
    state = 'choose option'
    return state


def wait_number(bot, update):
    try:
        number[update.message.from_user.id] = int(update.message.text)
        bot.send_message(update.message.from_user.id, "Введите список продуктов")
        state = 'wait products'
        return state
    except Exception as e:
        bot.send_message(update.message.from_user.id, "Пожалуйста, напишите число.")
    pass


def choose_option(bot, update):
    if update.message.text == 'Еще':
        state = 'wait number'
        bot.send_message(update.message.from_user.id, "Введите количество желаемых рецептов")
    else:
        state = 'init'
    return state





        
