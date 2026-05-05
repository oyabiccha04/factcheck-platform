import urllib.request
import urllib.parse
import re

events = [
    "RIZIN DECADE", "UFC 310", "平良達郎 ロイバル", "RIZIN 48", 
    "超RIZIN.3", "RIZIN 47", "ONE 167 武尊", "RIZIN 46",
    "RIZIN 45", "RIZIN LANDMARK 7", "RIZIN 44", "超RIZIN.2",
    "RIZIN 43", "RIZIN 42", "RIZIN 41", "RIZIN 40", 
    "RIZIN 39", "超RIZIN 朝倉未来 メイウェザー", "RIZIN 37", "RIZIN 36"
]

with open("yt_maeda_search.txt", "w", encoding="utf-8") as f:
    for event in events:
        query = f"前田日明 {event} 予想"
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            html = urllib.request.urlopen(req).read().decode("utf-8")
            titles_ids = re.findall(r'"videoId":"([^\"]+)".*?"title":\{"runs":\[\{"text":"(.*?)"\}\]', html)
            
            f.write(f"\n--- {event} ---\n")
            seen = set()
            count = 0
            for vid, title in titles_ids:
                if vid not in seen and len(title) > 5 and ("前田日明" in title or "予想" in title or "勝敗" in title or "前田" in title):
                    f.write(f"[{vid}] {title}\n")
                    seen.add(vid)
                    count += 1
                if count >= 3: break
        except Exception as e:
            f.write(f"Error: {e}\n")
