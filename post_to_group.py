""" Telegram messaging bot for Pandion related postings  """
# pylint: disable=C0103
# pylint: disable-msg=C0103
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
CHAT_ID = CPARSER.get('global', 'chat_id')

bot = telepot.Bot(API_KEY)

bot.sendMessage(CHAT_ID, "Hello there")
