# -*- coding: utf-8 -*-
"""The bot code."""
import itertools
import os
import time

import twitter
from us import states

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

TWENTY_MINUTES = 60 * 20

if __name__ == '__main__':
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    for state in itertools.cycle(states.STATES):
        api.PostUpdate('gay {}'.format(state.name))
        time.sleep(TWENTY_MINUTES)
