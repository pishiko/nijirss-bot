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

    def tweet(self, text: str, file_name: str):
        self.api.update_status_with_media(
            status=text,
            filename=file_name
        )


if __name__ == "__main__":
    Twitter().tweet("てすと #DEV", "out.png")
