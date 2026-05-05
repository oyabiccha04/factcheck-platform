import urllib.request
import urllib.parse
import re

queries = [
    "RIZIN.48 勝敗予想 サトシ グスタボ",
    "RIZIN.48 予想 井上 スーチョル",
    "超RIZIN.3 予想 扇久保 神龍",
    "超RIZIN.3 予想 久保 斎藤",
    "超RIZIN.3 勝敗予想 朝倉 平本",
]

with open("yt_48_sr3.txt", "w", encoding="utf-8") as f:
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
