import os

video_ids = [
    "OKVoHgi5mLI", "BGn5gMgcF1M", "8pvRpDAUS5A", # 45
    "CzxN_ibIKHM", "z278IdbQQvk", # 46
    "1EP1EOLHwFI", "N2-yzbRX824" # 47
]

cmds = []
for vid in video_ids:
    cmds.append(f'python -m yt_dlp --write-auto-sub --sub-lang ja --skip-download "https://www.youtube.com/watch?v={vid}" -o "{vid}.%(ext)s"')

with open("dl_yt_vtts.bat", "w") as f:
    f.write("\n".join(cmds))
