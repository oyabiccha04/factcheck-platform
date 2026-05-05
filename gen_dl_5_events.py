import os

video_ids = [
    "3fpw7fOYXpU",
    "rz9FT5kScn8",
    "pOs1V1ovBvg",
    "K08rsBqWEgs"
]

with open("dl_5_events.bat", "w", encoding="utf-8") as f:
    for vid in video_ids:
        f.write(f'yt-dlp --write-auto-sub --sub-lang ja,en --skip-download "https://www.youtube.com/watch?v={vid}"\n')
