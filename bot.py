import os
import telepot
from telepot import Bot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import time

# Load the file env from default location
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Configure bot handler
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = Bot(TOKEN)
print(bot.getMe())

# Handle message received
def on_chat_message(msg):
    print(msg)
    text = msg.get('text')

    parameters = get_command_parameters(text)
    content_type, chat_type, chat_id = telepot.glance(msg)
    if '/greetings' in text:
        bot.sendMessage(chat_id, "Hi {}, nice to meet you!".format(msg.get('from').get('first_name')))
    elif '/sayhelloto' in text:
        name = '' if len(parameters) == 0 else parameters[0]
        bot.sendMessage(chat_id, "Hi *{}*, nice to meet you!".format(name), parse_mode='Markdown')
    elif '/sendphoto' in text:
        category = '' if len(parameters) == 0 else parameters[0]
        bot.sendPhoto(chat_id, 'https://source.unsplash.com/featured/?{}'.format(category),
                      caption='Your <b>{}</b> photo is arrived'.format(category),
                      parse_mode='HTML'
                      )
    elif '/keyboard' in text:
        button1 = KeyboardButton(text="Yes")
        button2 = KeyboardButton(text="No")
        button3 = KeyboardButton(text="Don't know")
        keyboard = ReplyKeyboardMarkup(Keyboard=[
            [button1, button2, button3]
        ])

        bot.sendMessage(chat_id, 'This is a custom keyboard', reply_markup=keyboard)
    elif text.startswith('/'):
        bot.sendMessage(chat_id, "I'm sorry {} can't understand!".format(msg.get('from').get('first_name')))


def get_command_parameters(text:str) -> list:
    parameters = text.split()
    return parameters[1::]



# Starting message loop
MessageLoop(bot, on_chat_message).run_as_thread()
print ('Listening ...')
last_update_id = None
while 1:
    time.sleep(10)
