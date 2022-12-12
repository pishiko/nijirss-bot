from os import name
from pytube import Channel, YouTube
from random import choice
import io


def download_one(channel_id: str, out_name: str) -> YouTube:
    c = Channel(url=f"https://www.youtube.com/channel/{channel_id}")
    videos = [v for v in c.videos]
    videos += [v for v in c.streams]
    videos += [v for v in c.shorts]
    video = choice(videos)
    b = io.BytesIO()
    video.streams.filter(
        progressive=True, file_extension='mp4').first().download(output_path="./", filename=out_name)
    return video


if __name__ == "__main__":
    v = download_one("UCD-miitqNY3nyukJ4Fnf4_A", "video.mp4")
    print(v.title, v.length)
