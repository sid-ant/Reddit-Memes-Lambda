import praw
import os
import logging

logger = logging.getLogger()


def lambda_handler(event,context):
    try:
        dank = get_dem_memes()
        subsribers = get_chats()
        boys_go_deliver(dank,subsribers)
    except:
        raise
    
def get_dem_memes():
    clientid = os.environ['client_id']
    secret = os.environ['client_secret']
    user_agent = os.environ['useragent']
    reddit = praw.Reddit(client_id=clientid,
                     client_secret=secret,
                     user_agent=user_agent)

    logger.info(f"The reddit is in {reddit.read_only}")
    memes=[]
    for submission in reddit.subreddit("memes").rising(limit=5):
        memes.append(submission.url)
    return memes


# query database
def get_chats():
    return None


# make async calls to telegram api 
def boys_go_deliver(good_stuff,audience):
    return None