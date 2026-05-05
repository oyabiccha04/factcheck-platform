import json

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

filepath = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-landmark-13-fukuoka.json"
data = load_json(filepath)

preds = [
    {
        "statement_id": "stmt-lm13-horiguchi",
        "statement_date": "2026-04-06",
        "speaker": {
            "name": "堀口恭司",
            "role": "fighter",
            "affiliation": "ATT"
        },
        "content": {
            "raw_text": "シェードライフが2RでKO勝ちかな。久保は今回は策略があるから受けた試合だと思う。何かしらの罠を張っているんじゃないかなと思う。でも俺はそれも通用せずシェードライフが勝つと思う。",
            "normalized_text": "シェイドゥラエフが2R KO勝ちすると予想。久保が罠を張っていると分析しつつも、実力でシェイドゥラエフがそれを上回ると評価。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=GdkEG0nNq9U",
            "timestamp": "0:30"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "堀口恭司",
            "source_url": "https://www.youtube.com/watch?v=GdkEG0nNq9U",
            "source_ref": "stmt-lm13-horiguchi",
            "source_note": "YouTube動画より抽出（確認日：2026-05-05）。",
            "expected_winner": "ラジャブアリ・シェイドゥラエフ",
            "expected_method": "KO",
            "target": "ラジャブアリ・シェイドゥラエフ vs 久保優太",
            "expected_outcome": "シェイドゥラエフが2R KO勝ち",
            "deadline": "2026-04-12"
        },
        "verification": {
            "status": "pending",
            "verification_date": None,
            "winner": None,
            "method": None,
            "actual_outcome": "未開催（予定）",
            "notes": None
        }
    },
    {
        "statement_id": "stmt-lm13-hiramoto",
        "statement_date": "2026-04-01",
        "speaker": {
            "name": "平本蓮",
            "role": "fighter",
            "affiliation": "剛毅會"
        },
        "content": {
            "raw_text": "打撃だけでも久保よりシェイドライフのが上って言ってたな。シドラって雑魚クラに組みついた状態でやばいパタンチ打ってたけど、どのキックボクサーよりもパンチありそうだわ。",
            "normalized_text": "シェイドゥラエフの打撃とパワーを高く評価し、久保を上回っていると分析。シェイドゥラエフの勝利を予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=rP21QrDOFNs",
            "timestamp": "0:30"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "平本蓮",
            "source_url": "https://www.youtube.com/watch?v=rP21QrDOFNs",
            "source_ref": "stmt-lm13-hiramoto",
            "source_note": "YouTubeまとめ動画（5chスレ解説）での発言内容より抽出（確認日：2026-05-05）。",
            "expected_winner": "ラジャブアリ・シェイドゥラエフ",
            "expected_method": None,
            "target": "ラジャブアリ・シェイドゥラエフ vs 久保優太",
            "expected_outcome": "シェイドゥラエフが勝利",
            "deadline": "2026-04-12"
        },
        "verification": {
            "status": "pending",
            "verification_date": None,
            "winner": None,
            "method": None,
            "actual_outcome": "未開催（予定）",
            "notes": None
        }
    },
    {
        "statement_id": "stmt-lm13-jobin",
        "statement_date": "2026-04-05",
        "speaker": {
            "name": "ジョビン",
            "role": "analyst",
            "affiliation": "YouTuber・元総合格闘家"
        },
        "content": {
            "raw_text": "これまあでもセトライブ有利ですよね。もう勝てる気しれ、その久保に優太に限らず。どう考えたってやっぱシェードライフが勝つ。",
            "normalized_text": "シェイドゥラエフの圧倒的有利と予想。久保に限らず現在のシェイドゥラエフに勝てる選手はいないと高く評価。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=DJuvEBQ-9ME",
            "timestamp": "0:15"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ジョビン",
            "source_url": "https://www.youtube.com/watch?v=DJuvEBQ-9ME",
            "source_ref": "stmt-lm13-jobin",
            "source_note": "YouTube自動字幕より抽出（確認日：2026-05-05）。",
            "expected_winner": "ラジャブアリ・シェイドゥラエフ",
            "expected_method": None,
            "target": "ラジャブアリ・シェイドゥラエフ vs 久保優太",
            "expected_outcome": "シェイドゥラエフが勝利（圧倒的有利）",
            "deadline": "2026-04-12"
        },
        "verification": {
            "status": "pending",
            "verification_date": None,
            "winner": None,
            "method": None,
            "actual_outcome": "未開催（予定）",
            "notes": None
        }
    }
]

data["statements"] = preds

save_json(filepath, data)
print("Updated RIZIN LANDMARK 13")
