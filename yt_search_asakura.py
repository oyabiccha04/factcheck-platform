import urllib.request
import urllib.parse
import re

queries = [
    "RIZIN.42 勝敗予想 朝倉 元谷",
    "朝倉海 元谷友貴 予想",
    "RIZIN 42 朝倉海 元谷 予想"
]

with open("yt_search_42_asakura.txt", "w", encoding="utf-8") as f:
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
                if len(seen) >= 8: break
        except Exception as e:
            f.write(f"Error: {e}\n")
