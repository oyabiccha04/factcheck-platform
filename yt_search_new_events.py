import urllib.request
import urllib.parse
import re

queries = [
    "UFC 311 予想 中村倫也",
    "UFC 310 予想 朝倉海 パントージャ",
    "UFC 310 予想 朝倉海 堀口",
    "平良達郎 ロイバル 予想",
    "RIZIN DECADE 勝敗予想",
    "RIZIN 49 勝敗予想 ジョビン",
    "RIZIN 49 勝敗予想 石渡",
]

with open("yt_new_events.txt", "w", encoding="utf-8") as f:
    for q in queries:
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            html = urllib.request.urlopen(req).read().decode("utf-8")
            titles_ids = re.findall(r'"videoId":"([^\"]+)".*?"title":\{"runs":\[\{"text":"(.*?)"\}\]', html)
            
            f.write(f"\n--- Results for {q} ---\n")
            seen = set()
            for vid, title in titles_ids:
                if vid not in seen and len(title) > 5:
                    f.write(f"[{vid}] {title}\n")
                    seen.add(vid)
                if len(seen) >= 6: break
        except Exception as e:
            f.write(f"Error: {e}\n")
