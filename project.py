import telegram, config
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

import requests
import re
REQUEST_KWARGS={
    'proxy_url': 'https://36.67.248.203:3128/'
}

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    print('test')
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=update.message.chat_id, text='fuck you!')
    bot.send_photo(chat_id=chat_id, photo=url)
    #result = bop(bot, update)

def main():
    updater = Updater(
        '762284125:AAE_wRj0y9XMNPaZ53ExUO3oKX5Ekm97riw',
        request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
