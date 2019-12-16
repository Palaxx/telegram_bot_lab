import os
from telepot import Bot
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


# Starting message loop
print ('Listening ...')
last_update_id = None
while 1:
    messages = bot.getUpdates(last_update_id)

    print("Received {} messages".format(len(messages)))
    for message in messages:
        on_chat_message(message)
        last_update_id = message.get('update_id') + 1

    time.sleep(10)
