import urllib.request
import urllib.parse
import re

queries = [
    "RIZIN.45 予想 堀口 神龍",
    "RIZIN.45 予想 朝倉海 アーチュレッタ",
    "RIZIN.45 予想 堀口 朝倉海",
    "RIZIN 45 勝敗予想 ジョビン",
    "RIZIN 45 勝敗予想 石渡",
    "RIZIN.46 勝敗予想 鈴木 千裕 金原",
    "RIZIN 46 勝敗予想 ジョビン",
    "RIZIN 46 勝敗予想 くるみ",
    "RIZIN 46 勝敗予想 白川",
    "RIZIN.47 勝敗予想 堀口 ペティス",
    "RIZIN 47 勝敗予想 ジョビン",
    "RIZIN 47 予想 大沢",
]

with open("yt_45_46_47.txt", "w", encoding="utf-8") as f:
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
                if len(seen) >= 5: break
        except Exception as e:
            f.write(f"Error: {e}\n")
