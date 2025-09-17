import os
import threading
import tweepy

import post
import events



# Authorize Twitter with v1.1 API
def auth_v1(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

# Authorize Twitter with v2 API
def auth_v2(consumer_key, consumer_secret, access_token, access_token_secret, bearer_token):
    return tweepy.Client (
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret,
        bearer_token = bearer_token,
        return_type = None, 
    )

# Set up Twitter API clients
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
bearer_token = os.environ['BEARER_TOKEN'] 

twt_api = auth_v1(consumer_key, consumer_secret, access_token, access_token_secret)
twt_client = auth_v2(consumer_key, consumer_secret, access_token, access_token_secret, bearer_token)

# Parse event
parser = events.EventParser()
parsed_text, pics = parser.parse_event()

# Run the post in a separate thread
twt_thread = threading.Thread(
    target = post.twt_post,
    kwargs = {
        'twt_api': twt_api,
        'twt_client': twt_client,
        'parsed_text': parsed_text,
        'pics': pics,
        'log': True
    }
)

twt_thread.start()
twt_thread.join()
