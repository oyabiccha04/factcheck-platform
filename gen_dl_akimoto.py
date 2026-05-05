import os

video_ids = [
    "ChAWWqEmMtA",
    "ifLXeUg1qOg",
    "xppG1rPXvkw"
]

with open("dl_akimoto.bat", "w", encoding="utf-8") as f:
    for vid in video_ids:
        f.write(f'yt-dlp --write-auto-sub --sub-lang ja,en --skip-download "https://www.youtube.com/watch?v={vid}"\n')
