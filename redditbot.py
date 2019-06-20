import praw
import os
import logging
import requests 
import boto3 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

db = boto3.resource('dynamodb')
table = db.Table('Chats')

def lambda_handler(event,context):
    try:
        dank = get_dem_memes()
        subsribers = get_chats()
        #boys_go_deliver(dank,subsribers)
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
    logger.info(f"Got memes from reddit {memes}")
    return memes    


# query database
def get_chats():
    try:
        chats = table.scan(AttributesToGet=['chatid'])
        for chat in chats:
            logger.info(f"chat type is {type(chat)} and value is {chat}")
    except:
        logger.info("couldn't query db to get chats")
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