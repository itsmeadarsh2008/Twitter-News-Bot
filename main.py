import tweepy
import schedule
import bbc_feeds
import time
import random
# reverting back
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN

client = tweepy.Client(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token=ACCESS_TOKEN,
                    access_token_secret=ACCESS_TOKEN_SECRET)

def tweet_news():
    stories = bbc_feeds.news().all(limit=1)
    client.create_tweet(text=''.join([f"📰{story.title}📰\n{story.summary}\n{random.choice(['Donate BTC: bc1q0v5a27rk7s8xq6wzv5zhkhau2swj88c8m4k6dl',story.link])}" for story in stories]))


schedule.every(30).minutes.do(tweet_news)

print('BOT RUNNING: %s' % schedule.jobs)
while True:
    schedule.run_pending()
    time.sleep(1)