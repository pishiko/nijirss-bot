import csv
import json
import requests

with open('./util/tags.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    tags = [row for row in reader]

try:
    resp = requests.get("https://api.itsukaralink.jp/v1.2/livers.json")
    livers = json.loads(resp.text)
    with open("./util/livers.json", mode="w", encoding="utf-8") as f:
        json.dump(livers, f, indent=2, ensure_ascii=False)
except:
    print("fetch failed")
    with open('./util/livers.json', encoding="utf-8") as f:
        livers = json.loads(f.read())

out = {
    "livers": []
}

for liver in livers["data"]["liver_relationships"]:
    name = liver["liver"]["name"]
    youtube = liver["liver_youtube_channel"]["channel"]
    tag = "#にじさんじ"

    ftags = list(filter(lambda tag: tag[0] == name, tags))
    if ftags:
        tag = ftags[0][1]
    out["livers"].append({
        "name": name,
        "channel_id": youtube,
        "tag": tag
    })
with open("./data.json", mode="w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"complete size:{len(out['livers'])}")
