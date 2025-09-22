import tweepy
from tweepy import TweepyException

import bot_logging



def twt_post(twt_api: tweepy.API, twt_client: tweepy.Client, parsed_text, pics, log=False) -> None:
    """
    :param twt_api: Authenticated API of the bot
    :param twt_client: Authenticated client of the bot on Twitter
    :param parsed_text: Text for bot to post
    :param pics: File paths to the pics for the bot to post
    :param log: Whether to log info messages
    """
    try:
        twt_media_ids = []
        for p in pics:
            twt_media_ids.append(twt_api.media_upload(filename=p).media_id_string)

        res = twt_client.create_tweet(text=parsed_text, media_ids=twt_media_ids)
        if res.errors:
            bot_logging.log_error_twt(res)
        elif log:
            bot_logging.log_info_twt(res.data)
    except TweepyException as e:
        bot_logging.log_error_twt(f'bot.py: {e}')


