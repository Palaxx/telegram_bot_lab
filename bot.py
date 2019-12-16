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

# Handle message received
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, "Hi {}, nice to meet you!".format(msg.get('from').get('first_name')))


# Starting message loop
MessageLoop(bot, on_chat_message).run_as_thread()
print ('Listening ...')
last_update_id = None
while 1:
    time.sleep(10)
