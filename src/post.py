import atproto
import tweepy
from tweepy import TweepyException

import bot_logging



def twt_post(twt_api: tweepy.API, parsed_text, pics, log=False) -> None:
    """
    Send a tweet with media using v1.1 API only.
    
    :param twt_api: Authenticated Tweepy API client (v1.1)
    :param parsed_text: Text content for the tweet
    :param pics: List of file paths to media
    :param log: Whether to log the response or errors
    """
    try:
        twt_media_ids = []
        for p in pics:
            media = twt_api.media_upload(filename=p)
            twt_media_ids.append(media.media_id_string)

        res = twt_api.update_status(status=parsed_text, media_ids=twt_media_ids)

        if log:
            bot_logging.log_info_twt(res)
    except TweepyException as e:
        bot_logging.log_error_twt(f'bot.py: {e}')

