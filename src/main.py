import os
import tweepy

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    user = api.verify_credentials()
    if user:
        print(f"✅ Authenticated as {user.screen_name}")
    else:
        print("❌ Authentication failed.")
except Exception as e:
    print(f"❌ Exception: {e}")
