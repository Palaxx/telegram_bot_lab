import os
from telepot import Bot
from telepot.loop import MessageLoop
import time

# Load the file env from default localtion
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Configure bot handler
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = Bot(TOKEN)
print(bot.getMe())

# Handle message received
def on_chat_message(msg):
    pass


# Starting message loop
# MessageLoop(bot, on_chat_message).run_as_thread()

# Blocking loop MessageLoop(bot, on_chat_message).run_forever()
print ('Listening ...')
while 1:
    # message = bot.getUpdates()
    # print(message)
    time.sleep(10)
