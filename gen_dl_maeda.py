import os

video_ids = [
    "F6vVJw6Umnk", "7VGbqPuKspI", "pGjoR7UqOwc", "mkkXQO7jct4", 
    "8lUwXIVS-2E", "ESYIALDnsqw", "8zK2kdq--ZA"
]

cmds = []
for vid in video_ids:
    cmds.append(f'python -m yt_dlp --write-auto-sub --sub-lang ja --skip-download "https://www.youtube.com/watch?v={vid}" -o "maeda_{vid}.%(ext)s"')

with open("dl_maeda_vtts.bat", "w") as f:
    f.write("\n".join(cmds))
