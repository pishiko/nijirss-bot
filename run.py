import traceback
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

    try_counter = 0
    while try_counter < RETRY_MAX:
        print(f"Start try:{try_counter}")
        try:
            with open(INPUT_DATA, encoding="utf-8") as f:
                data = json.load(f)
            liver = choice(data["livers"])
            video = download_one(liver["channel_id"], MOVIE_NAME)
            time = randint(1, video.length)
            create_image(MOVIE_NAME, IMAGE_NAME, time)
            publish_date = video.publish_date.strftime('%Y年%m月%d日') if video.publish_date else ''
            break
        except Exception as _:
            try_counter += 1
            post_hook(f"try:{try_counter}\n```{traceback.format_exc()}```")
    else:
        post_hook(f"@everyone EXIT")
        return

    twitter = Twitter()
    text = f"{publish_date} {liver['tag']}\n{video.watch_url}&t={time}s"
    twitter.tweet(text, IMAGE_NAME)
    post_hook(f"#SUCCESS:{video.title}({video.watch_url}&t={time}s)")


if __name__ == "__main__":
    main()
