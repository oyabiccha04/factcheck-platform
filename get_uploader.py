import urllib.request
import re

url = "https://www.youtube.com/watch?v=ThsvL2Y7CPI"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    html = urllib.request.urlopen(req).read().decode("utf-8")
    m = re.search(r'<title>(.*?)</title>', html)
    if m:
        title = m.group(1).replace(" - YouTube", "")
    
    m2 = re.search(r'"author":"([^"]+)"', html)
    author = m2.group(1) if m2 else "Unknown"

    with open("uploader_out.txt", "w", encoding="utf-8") as f:
        f.write(f"Title: {title}\nAuthor: {author}\n")
except Exception as e:
    print(e)
