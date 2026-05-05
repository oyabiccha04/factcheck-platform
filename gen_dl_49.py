import os

video_ids = ["as_ot9pNXIs", "dDDq7hGWscE", "qKHHCjT2Oac"]

cmds = []
for vid in video_ids:
    cmds.append(f'python -m yt_dlp --write-auto-sub --sub-lang ja --skip-download "https://www.youtube.com/watch?v={vid}" -o "{vid}.%(ext)s"')

with open("dl_49_vtts.bat", "w") as f:
    f.write("\n".join(cmds))
