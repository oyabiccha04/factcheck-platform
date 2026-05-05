import json
from youtube_transcript_api import YouTubeTranscriptApi

videos = [
    {"id": "0kAn-7mH76o", "time": 255, "name": "朝倉未来"},
    {"id": "A_0_q_hV_60", "time": 525, "name": "矢地祐介"},
    {"id": "O9vYF_6v8Xg", "time": 740, "name": "石渡伸太郎"},
    {"id": "FOf68n3-v6I", "time": 495, "name": "川尻達也"},
]

for v in videos:
    print(f"\n--- {v['name']} (Video ID: {v['id']}) ---")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(v["id"], languages=["ja"])
        # Find entries around the time
        start_time = max(0, v["time"] - 90)
        end_time = v["time"] + 90
        
        texts = []
        for t in transcript:
            if start_time <= t["start"] <= end_time:
                texts.append(f"[{int(t['start'])}s] {t['text']}")
        
        if texts:
            print("\n".join(texts))
        else:
            print("No transcript found in that time range.")
    except Exception as e:
        print(f"Error: {e}")
