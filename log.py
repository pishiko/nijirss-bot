from os import getenv
from dotenv import load_dotenv
from requests import post

load_dotenv()
HOOK_URL = getenv("HOOK_URL")
if not HOOK_URL:
    raise RuntimeError("no env HOOK_URL")


def post_hook(msg: str, isprint=True):
    print(msg)
    try:
        post(url=HOOK_URL, json={"content": msg})
    except:
        print("HOOK FAILED")
    return


if __name__ == "__main__":
    post_hook("わかります")
