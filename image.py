from os import getenv
import subprocess
from dotenv import load_dotenv

load_dotenv()

ffmpeg = getenv("FFMPEG_PATH")
if not ffmpeg:
    ffmpeg = "ffmpeg"


def create_image(in_name: str, out_name: str, time: int):
    subprocess.check_call(
        f"{ffmpeg} -y -i {in_name} -ss {time} -t 1 -r 1 -f image2 -loglevel error {out_name}", shell=True)


if __name__ == "__main__":
    create_image("video.mp4", "out.png", 3000)
