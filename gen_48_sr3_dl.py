import os

video_ids = [
    "rFcrXlSnrmg", "cD423PeaXow", "acUsEF8pOTo", # 48
    "DmUyv_FlDpE", "WgaHYE0VrxQ", "j9H1Brwm9j4", "W45XBrygwhs" # SR3
]

cmds = []
for vid in video_ids:
    cmds.append(f'python -m yt_dlp --write-auto-sub --sub-lang ja --skip-download "https://www.youtube.com/watch?v={vid}" -o "{vid}.%(ext)s"')

with open("dl_48_sr3.bat", "w") as f:
    f.write("\n".join(cmds))
