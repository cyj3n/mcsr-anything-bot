import atproto
import tweepy

def twt_post(twt_api: tweepy.API, twt_client: tweepy.Client, parsed_text, pics, log=False) -> None:
    """
    Send a random tweet from the ProjectMoon Anything Bot and logs the response
    :param twt_api: Authenticated API of the bot
    :param twt_client: Authenticated client of the bot on Twitter
    :param parsed_text: Text for bot to post
    :param pics: File paths to the pics for the bot to post
    :return: None
    """
