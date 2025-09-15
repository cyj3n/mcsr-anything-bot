import os
import random
import requests
import threading
import tweepy

import post
import events



# Pick a random image/video from the 'assets' folder
def get_random_media():
    path = 'assets'
    objects = os.listdir(path)
    media = random.choice(objects)
    return os.path.join(path, media)


# Authorize Twitter with v1.1 API
def auth_v1(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

# Authorize Twitter with v2 API
def auth_v2(consumer_key, consumer_secret, access_token, access_token_secret):
    return tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret,
        return_type=requests.Response,
    )

# Set up Twitter API clients
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

twt_api = auth_v1(consumer_key, consumer_secret, access_token, access_token_secret)
twt_client = auth_v2(consumer_key, consumer_secret, access_token, access_token_secret)


# Parse event
parser = events.EventParser()
parsed_text, pics = parser.parse_event()

# Run the post in a separate thread
twt_thread = threading.Thread(
    target=post.twt_post,
    kwargs={
        'twt_api': twt_api,
        'twt_client': twt_client,
        'parsed_text': parsed_text,
        'pics': pics
    }
)

twt_thread.start()
twt_thread.join()
