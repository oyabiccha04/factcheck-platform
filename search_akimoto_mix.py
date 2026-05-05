import urllib.request
import json
import urllib.parse

def search_yt(query, max_results=20):
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
    "秋元 パッチーミックス 予想",
    "秋元強真 パッチー・ミックス 予想",
    "RIZIN 52 秋元 予想"
]

with open("yt_search_akimoto_mix.txt", "w", encoding="utf-8") as f:
    for q in queries:
        f.write(f"=== {q} ===\n")
        res = search_yt(q)
        for r in res:
            f.write(r + "\n")
        f.write("\n")
