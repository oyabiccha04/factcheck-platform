import json
import urllib.request
import re

video_ids = [
    "7uV8-M6b9sQ", "F3xZ8Tz7r_E", "L_6n_U_Xv3s", "7p_G7z8pX3A", "f0_M0Kk_D6E",
    "N4l_f8p9W-s", "9_D-C_H9B20", "NnF_A_U4K6c", "ZfA7X_e_Oms", "3u_Kx8XQ_Qc",
    "Yf_G7QfO6t8", "YpLgH7u_m-I", "FmS3m61q-jQ", "0hYm6lZ-m-o", "vV9o9W_Yl7k",
    "7uV8GZ4fV9M"
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
