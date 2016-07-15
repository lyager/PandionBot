""" Telegram listener test """
# pylint: disable=C0103
# pylint: disable-msg=C0103
from pprint import pprint
import time
import ConfigParser
import sys
import logging
import telepot

logging.basicConfig()

LOG = logging.getLogger()
CONF_FILE = 'pandion_bot.conf'

CPARSER = None
try:
    CPARSER = ConfigParser.ConfigParser()
    CPARSER.read(CONF_FILE)
except ConfigParser.Error as exc:
    LOG.critical("Unable to parse %s: %s", CONF_FILE, exc)
    sys.exit(1)

API_KEY = CPARSER.get('global', 'api_key')


def got_message(msg):
    """ Callback, got message from Telegram """
    pprint(msg)
    if 'entities' in msg:
        if 'type' in msg['entities']:
            if msg['entities']['type'] == "bot_command":
                print "Got command: {}".format(msg['text'])
    else:
        bot.sendMessage(msg['from']['id'],
                        "Hi {}, you look great!"
                        .format(msg['from']['username']))


bot = telepot.Bot(API_KEY)

bot.message_loop(got_message)
while True:
    updates = bot.getUpdates()
    if updates:
        pprint(updates)
    time.sleep(5)
