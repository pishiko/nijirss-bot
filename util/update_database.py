import csv
import json
import requests

with open('./util/tags.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    tags = [row for row in reader]

try:
    resp = requests.get("https://www.nijisanji.jp/api/livers?limit=300&orderKey=debut_at&order=asc&affiliation=nijisanji&locale=ja&includeHidden=true")
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

for liver in livers:
    name = liver["name"]
    youtube = liver["socialLinks"]["youtube"]
    if youtube:
        youtube = youtube.replace("https://www.youtube.com/channel/","")
    tag = "#にじさんじ"

    ftags = list(filter(lambda tag: tag[0] == name, tags))
    if ftags:
        tag = ftags[0][1]
    else:
        print(f'{name} is not in csv.')
        continue
    out["livers"].append({
        "name": name,
        "channel_id": youtube,
        "tag": tag
    })
with open("./data.json", mode="w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"complete size:{len(out['livers'])}")
