import tweepy
import bbc_feeds
import time
import random
import os

client = tweepy.Client(consumer_key=os.getenv('CONSUMER_KEY'),
                    consumer_secret=os.getenv('CONSUMER_SECRET'),
                    access_token=os.getenv('ACCESS_TOKEN'),
                    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))

def tweet_news():
    stories = bbc_feeds.news().all(limit=1)
    client.create_tweet(text=''.join([f"📰{story.title}📰\n{story.summary}\n{random.choice(['Donate BTC: bc1q0v5a27rk7s8xq6wzv5zhkhau2swj88c8m4k6dl',story.link])}" for story in stories]))


if __name__ == '__main__':
    tweet_news()