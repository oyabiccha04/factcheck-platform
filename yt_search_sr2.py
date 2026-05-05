import urllib.request
import urllib.parse
import re

queries = [
    "超RIZIN.2 勝敗予想 ジョビン",
    "超RIZIN.2 勝敗予想 くるみ",
    "超RIZIN.2 勝敗予想 白川",
    "朝倉未来 ケラモフ 予想",
    "堀口恭司 神龍誠 予想 ジョビン",
    "超RIZIN.2 予想 川尻",
    "超RIZIN.2 予想 大沢"
]

with open("yt_super_rizin_2.txt", "w", encoding="utf-8") as f:
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
