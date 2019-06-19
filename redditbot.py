import praw
import os
import logging

clientid = os.environ['client_id']
secret = os.environ['client_secret']
user_agent = os.environ['useragent']

reddit = praw.Reddit(client_id=clientid,
                     client_secret=secret,
                     user_agent=user_agent)

print(reddit.read_only)

for submission in reddit.subreddit("memes").rising(limit=5):
    print(submission.url)
