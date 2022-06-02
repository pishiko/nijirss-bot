from youtube import download_one
from image import create_image
from twitter import Twitter
import json
from random import choice, randint
import os
from log import post_hook

INPUT_DATA = "data.json"
MOVIE_NAME = "video.mp4"
IMAGE_NAME = "out.png"

RETRY_MAX = 5


def main():

    counter = 0
    while counter < RETRY_MAX:
        print(f"Start try:{counter}")
        try:
            with open(INPUT_DATA, encoding="utf-8") as f:
                data = json.load(f)
            liver = choice(data["livers"])
            video = download_one(liver["channel_id"], MOVIE_NAME)
            time = randint(1, video.length)
            create_image(MOVIE_NAME, IMAGE_NAME, time)
            break
        except Exception as e:
            post_hook(f"catch failed : {os.path.basename(__file__)}{str(e)}")
            counter += 1
    else:
        post_hook(f"@everyone EXIT : failed {RETRY_MAX}times")
        return

    twitter = Twitter()
    text = f" {liver['tag']}"
    twitter.tweet(text, IMAGE_NAME)
    post_hook(f"#SUCCESS:{video.title}({video.watch_url}&t={time}s)")


if __name__ == "__main__":
    main()
