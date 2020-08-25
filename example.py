import pychatapi
from pychatapi import Client

import random, logging
logging.basicConfig(level=logging.ERROR)

client = Client("BOT-API-TEST", "#000000")

@client.listener
def main(msg):

    if msg.content == "!flip":
        client.send(random.choice(["heads", "tails"]))

if __name__ == '__main__':
    main()
