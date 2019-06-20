import praw
import os
import logging
import requests 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    try:
        dank = get_dem_memes()
        subsribers = get_chats()
        boys_go_deliver(dank,subsribers)
    except:
        logger.log("opps, something bad happened")
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
    for submission in reddit.subreddit("memes").top('hour',limit=10):
        if submission.find("i.redd.it")!=-1:
            memes.append(submission.url)
    memes = memes[:5]
    return memes    


# query database
def get_chats():
    return None


# make async calls to telegram api 
def boys_go_deliver(good_stuff,audience):
    accesscode = os.environ['accesscode']
    try:
        url = f"https://api.telegram.org/bot{accesscode}/sendPhoto"
        logger.info(f"url formed is {url}")
        for stuff in good_stuff:
            response = requests.post(url, data={'chat_id':chat_id,'photo':stuff})
        logger.info(f"Successfully sent message! {good_stuff}")
    except RequestException as e:
        logger.error(f"Couldn't send reply {e}")
    return None