import os
import telepot

from telepot import Bot
from telepot.loop import MessageLoop
import time

# Load the file env from default location
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Configure bot handler
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = Bot(TOKEN)
print(bot.getMe())
game_name = os.environ['GAME_NAME']


# Handle message received
def on_chat_message(msg):
    text = msg.get('text')
    content_type, chat_type, chat_id = telepot.glance(msg)
    if '/startgame' in text:
        bot.sendGame(chat_id, game_name)
    elif text.startswith('/'):
        bot.sendMessage(chat_id, "I'm sorry {} can't understand!".format(msg.get('from').get('first_name')))


def on_callback_query(msg):
    query_id = msg.get('id')
    if msg.get('game_short_name') != game_name:
        bot.answerCallbackQuery(query_id, text='Sorry {} is not an available game'.format(msg.get('game_short_name')))
    else:
        from_id = msg.get('from').get('id')
        chat_id = msg.get('message').get('chat').get('id')
        message_id = msg.get('message').get('message_id')
        # Send info on query string, these ids is required to save the highscore.
        game_url = os.environ['GAME_URL'] + "?from_id={}&chat_id={}&message_id={}".format(from_id, chat_id, message_id)
        bot.answerCallbackQuery(query_id, url=game_url)


# Starting message loop
MessageLoop(bot, {
    'chat': on_chat_message,
    'callback_query': on_callback_query
}).run_as_thread()
print('Listening ...')
last_update_id = None
while 1:
    time.sleep(10)
