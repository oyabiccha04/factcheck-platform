import urllib.request
import re

url = 'https://www.youtube.com/results?search_query=RIZIN.37+%E5%8B%9D%E6%95%97%E4%BA%88%E6%83%B3'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    titles = re.findall(r'\"title\":\{\"runs\":\[\{\"text\":\"(.*?)\"\}\]', html)
    
    unique_titles = []
    for t in titles:
        if t not in unique_titles:
            unique_titles.append(t)
            
    with open('yt_titles.txt', 'w', encoding='utf-8') as f:
        for t in unique_titles[:25]:
            f.write("- " + t + "\n")
except Exception as e:
    print(e)
