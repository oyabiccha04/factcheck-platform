import os

video_ids = [
    "QUX7tGg0PyA", # 朝倉未来
    "wjQJDW3jQJY", # ジョビン
    "tf0-buC1RPk", # 格闘BuZZ NEWS
    "twizgK-OMFo", # 朝倉海のUFCデビュー戦 勝敗予想
]

cmds = []
for vid in video_ids:
    cmds.append(f'python -m yt_dlp --write-auto-sub --sub-lang ja --skip-download "https://www.youtube.com/watch?v={vid}" -o "{vid}.%(ext)s"')

with open("dl_ufc310_vtts.bat", "w") as f:
    f.write("\n".join(cmds))
