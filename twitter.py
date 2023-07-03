from os import getenv
from dotenv import load_dotenv
import tweepy

load_dotenv()
CONSUMER_KEY = getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = getenv("TWITTER_ACCESS_SECRET")


class Twitter():
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                                   access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)

    def tweet(self, text: str, file_name: str):
        media =  self.api.simple_upload(filename=file_name)
        if media is None:
            raise Exception("media is None")
        self.client.create_tweet(text=text, media_ids=[media.media_id])

if __name__ == "__main__":
    Twitter().tweet("test #dev", "youtuber_virtual.png")
