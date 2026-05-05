import urllib.request
import re

video_ids = [
    # UFC 311
    # no youtube links in ufc-311.json
    
    # UFC 310
    # no youtube links in ufc-310.json
    
    # UFC FN 244
    # no youtube links in ufc-fight-night-244.json
    
    # RIZIN 49
    "F7mN8x7F6-M", "Pq_Zf_A2W6Y", "3X_VfL7K9E8"
]

for vid in video_ids:
    url = f"https://www.youtube.com/watch?v={vid}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = urllib.request.urlopen(req).read().decode("utf-8")
        m = re.search(r'<title>(.*?)</title>', html)
        title = m.group(1).replace(" - YouTube", "") if m else "Unknown Title"
        print(f"{vid}: {title}")
    except Exception as e:
        print(f"{vid}: Error {e}")
