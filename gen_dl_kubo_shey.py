import os

video_ids = [
    "rP21QrDOFNs",
    "9kAwMKE-Ddg",
    "GdkEG0nNq9U",
    "yaSKtzqyJ9U",
    "DJuvEBQ-9ME"
]

with open("dl_kubo_shey.bat", "w", encoding="utf-8") as f:
    for vid in video_ids:
        f.write(f'yt-dlp --write-auto-sub --sub-lang ja,en --skip-download "https://www.youtube.com/watch?v={vid}"\n')
