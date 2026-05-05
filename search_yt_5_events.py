import urllib.request
import json
import urllib.parse

def search_yt(query, max_results=15):
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded_query}&sp=EgQQARgB"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        results = []
        parts = html.split('{"videoRenderer":{')
        for part in parts[1:max_results+1]:
            try:
                vid_id = part.split('"videoId":"')[1].split('"')[0]
                title = part.split('"title":{"runs":[{"text":"')[1].split('"')[0]
                uploader = part.split('"ownerText":{"runs":[{"text":"')[1].split('"')[0]
                results.append(f"{vid_id} | {uploader} | {title}")
            except Exception:
                pass
        return results
    except Exception as e:
        return [str(e)]

queries = [
    "RIZIN LANDMARK 13 予想",
    "RIZIN LANDMARK 13 久保 シェイドゥラエフ 予想",
    "RIZIN 52 予想",
    "UFC 堀口恭司 アルバジ 予想",
    "RIZIN師走の超強者祭り 予想",
    "UFC カタール 堀口恭司 予想",
    "Kamaru Usman Kyoji Horiguchi prediction"
]

with open("yt_search_5_events.txt", "w", encoding="utf-8") as f:
    for q in queries:
        f.write(f"=== {q} ===\n")
        res = search_yt(q)
        for r in res:
            f.write(r + "\n")
        f.write("\n")
