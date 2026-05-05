import json

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

filepath = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-52.json"
data = load_json(filepath)

preds = [
    {
        "statement_id": "stmt-r52-jobin",
        "statement_date": "2026-03-01",
        "speaker": {
            "name": "ジョビン",
            "role": "analyst",
            "affiliation": "YouTuber・元総合格闘家"
        },
        "content": {
            "raw_text": "組の面ではパッチミックスでパッチミックス1本勝ち圧勝かなと正直思ってたけど青き深夜が入ってきたことによってちょっと分からんなって思ってきた。ただやっぱり勝敗予想ってなったらパッチミックスかなと思うけど",
            "normalized_text": "パッチー・ミックスの勝利を予想。秋元が青木真也と練習したことで期待感はあるものの、パッチー・ミックスの組みの強さが上回ると分析。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=ifLXeUg1qOg",
            "timestamp": "0:50"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ジョビン",
            "source_url": "https://www.youtube.com/watch?v=ifLXeUg1qOg",
            "source_ref": "stmt-r52-jobin",
            "source_note": "YouTube自動字幕より抽出（確認日：2026-05-05）。",
            "expected_winner": "パッチー・ミックス",
            "expected_method": None,
            "target": "秋元強真 vs パッチー・ミックス",
            "expected_outcome": "パッチー・ミックスが勝利",
            "deadline": "2026-03-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2026-03-07",
            "winner": "秋元強真",
            "method": "TKO",
            "actual_outcome": "秋元強真がTKO勝ち",
            "notes": "予想外れ。"
        }
    },
    {
        "statement_id": "stmt-r52-2ch",
        "statement_date": "2026-02-20",
        "speaker": {
            "name": "ネットの反応（2chまとめ）",
            "role": "fan",
            "affiliation": "格闘技ファン"
        },
        "content": {
            "raw_text": "ベラ時代の仕上がりきたら厳しすぎる。超強い。勝負論なさすぎる。秋元潰すマッチで草。秋元が勝つのは厳しすぎる。",
            "normalized_text": "パッチー・ミックスの圧倒的有利を予想。ファン層の大多数が秋元にとって厳しすぎるマッチアップだと評価。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=xppG1rPXvkw",
            "timestamp": "0:10"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ネットの反応（2chまとめ）",
            "source_url": "https://www.youtube.com/watch?v=xppG1rPXvkw",
            "source_ref": "stmt-r52-2ch",
            "source_note": "YouTube 2chまとめ動画より抽出（確認日：2026-05-05）。",
            "expected_winner": "パッチー・ミックス",
            "expected_method": None,
            "target": "秋元強真 vs パッチー・ミックス",
            "expected_outcome": "パッチー・ミックスが勝利（圧倒的有利）",
            "deadline": "2026-03-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2026-03-07",
            "winner": "秋元強真",
            "method": "TKO",
            "actual_outcome": "秋元強真がTKO勝ち",
            "notes": "予想外れ。大番狂わせとなった。"
        }
    },
    {
        "statement_id": "stmt-r52-tapology",
        "statement_date": "2026-03-06",
        "speaker": {
            "name": "Tapology",
            "role": "community",
            "affiliation": "MMA Database"
        },
        "content": {
            "raw_text": "コミュニティピックにおいてパッチー・ミックスが71%、秋元強真が29%と予想されていました。",
            "normalized_text": "Tapologyコミュニティ予想の71%がパッチー・ミックスの勝利を支持。"
        },
        "source": {
            "type": "article",
            "url": "https://www.tapology.com/fightcenter/bouts/1094626-rizin-52-kyoma-the-hunter-akimoto-vs-patchy-no-love-mix",
            "timestamp": "2026-03-06"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "Tapologyコミュニティ",
            "source_url": "https://www.tapology.com/fightcenter/bouts/1094626-rizin-52-kyoma-the-hunter-akimoto-vs-patchy-no-love-mix",
            "source_ref": "stmt-r52-tapology",
            "source_note": "Web検索結果より抽出（確認日：2026-05-05）。Tapologyコミュニティピック。",
            "expected_winner": "パッチー・ミックス",
            "expected_method": None,
            "target": "秋元強真 vs パッチー・ミックス",
            "expected_outcome": "パッチー・ミックスが勝利（71%の支持）",
            "deadline": "2026-03-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2026-03-07",
            "winner": "秋元強真",
            "method": "TKO",
            "actual_outcome": "秋元強真がTKO勝ち",
            "notes": "多数派の予想が外れた。"
        }
    }
]

# Avoid duplicates
existing_ids = {s["statement_id"] for s in data.get("statements", [])}
for p in preds:
    if p["statement_id"] not in existing_ids:
        data["statements"].append(p)

save_json(filepath, data)
print("Updated RIZIN 52")
