import sys
from youtube_transcript_api import YouTubeTranscriptApi

video_ids = ["uTo51AWHARM", "LYm_VDajMM8"]

for vid in video_ids:
    print(f"\n--- Transcript for {vid} ---")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(vid, languages=["ja"])
        text = " ".join([t["text"] for t in transcript])
        print(text[:500] + "...")
    except Exception as e:
        print(f"Error: {e}")
