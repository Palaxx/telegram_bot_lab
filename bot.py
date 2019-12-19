import os
import telepot
import schedule
import request

from telepot import Bot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import time

# Load the file env from default location
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Configure bot handler
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = Bot(TOKEN)
print(bot.getMe())

registrations = {}
def get_price(crypto:str) -> float:
    request
    pass
# Handle message received
def on_chat_message(msg):
    text = msg.get('text')
    parameters = get_command_parameters(text)
    content_type, chat_type, chat_id = telepot.glance(msg)
    if '/registeralert' in text:
        button_btc = InlineKeyboardButton(text='Bitcoin', callback_data='BTC')
        button_eth = InlineKeyboardButton(text='Etherium', callback_data='ETH')
        button_vet = InlineKeyboardButton(text='VeChain', callback_data='VET')
        button_bat = InlineKeyboardButton(text='Basic Attention Token', callback_data='BAT')
        keyboard = InlineKeyboardMarkup(inline_keyboard = [
            [button_btc], [button_eth], [button_vet], [button_bat]
        ])
        bot.sendMessage(chat_id, 'In which cryptocurrency you want to be notified?', reply_markup=keyboard)
    elif '/getprice' in text:
        value = get_price(parameters[0])
    elif text.startswith('/'):
        bot.sendMessage(chat_id, "I'm sorry {} can't understand!".format(msg.get('from').get('first_name')))

def on_callback_query(msg):
    chat_id = msg.get('from').get('id')
    print(chat_id)
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    registrations[chat_id] = query_data
    bot.answerCallbackQuery(query_id, text='Got it! {} choice saved'.format(query_data))



def get_command_parameters(text:str) -> list:
    parameters = text.split()
    return parameters[1::]

def scheduled_message():
    print('Send scheduled message')
    for chat_id, crypto in registrations.items():
        print(chat_id, crypto)
    # bot.sendMessage(os.getenv('MY_CHAT_ID'), 'Hi, this is a scheduled message')

schedule.every(1).minutes.do(scheduled_message)

# Starting message loop
MessageLoop(bot, {
    'chat' : on_chat_message,
    'callback_query' : on_callback_query
}).run_as_thread()
print ('Listening ...')
last_update_id = None
while 1:
    schedule.run_pending()
    time.sleep(10)
