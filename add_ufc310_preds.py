import json

file_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\ufc-310.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

new_statements = [
    {
        "statement_id": "stmt-ufc-310-new-001",
        "statement_date": "2024-12-01",
        "speaker": {
            "name": "朝倉未来",
            "role": "fighter",
            "affiliation": "JAPAN TOP TEAM / 格闘家・YouTuber"
        },
        "content": {
            "raw_text": "こういうアーチレタとかパントージャみたいなタイプは弟が最も得意な相手だと思ってるんで普通に勝つと思いますけど",
            "normalized_text": "パントージャのようなタイプは朝倉海が最も得意としており、普通に勝つと予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=QUX7tGg0PyA",
            "timestamp": "06:44"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "朝倉未来",
            "source_url": "https://www.youtube.com/watch?v=QUX7tGg0PyA",
            "source_ref": "stmt-ufc-310-new-001",
            "source_note": "YouTube勝敗予想動画から抽出",
            "expected_winner": "朝倉海",
            "expected_method": "Decision/KO",
            "target": "アレシャンドレ・パントージャ vs 朝倉海",
            "expected_outcome": "朝倉海の勝利（普通に勝つ）",
            "deadline": "2024-12-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-12-08",
            "winner": "アレシャンドレ・パントージャ",
            "method": "Submission",
            "actual_outcome": "パントージャが2R一本勝ち",
            "notes": "予想外れ。得意なタイプと分析していたが、パントージャの寝技に捕まった。"
        }
    },
    {
        "statement_id": "stmt-ufc-310-new-002",
        "statement_date": "2024-12-05",
        "speaker": {
            "name": "石渡伸太郎",
            "role": "coach",
            "affiliation": "CAVE"
        },
        "content": {
            "raw_text": "5ラウンド右のストレートから返しの左フックでKOです",
            "normalized_text": "打撃戦や組みの攻防が続く中、5ラウンドにパントージャがパンチでKO勝利すると予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=tf0-buC1RPk",
            "timestamp": "10:30"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "石渡伸太郎",
            "source_url": "https://www.youtube.com/watch?v=tf0-buC1RPk",
            "source_ref": "stmt-ufc-310-new-002",
            "source_note": "YouTube勝敗予想動画から抽出",
            "expected_winner": "アレシャンドレ・パントージャ",
            "expected_method": "KO",
            "target": "アレシャンドレ・パントージャ vs 朝倉海",
            "expected_outcome": "パントージャの5R KO勝ち",
            "deadline": "2024-12-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-12-08",
            "winner": "アレシャンドレ・パントージャ",
            "method": "Submission",
            "actual_outcome": "パントージャが2R一本勝ち",
            "notes": "勝者予想は的中。フィニッシュラウンド・方法は異なった。"
        }
    }
]

data.setdefault("statements", []).extend(new_statements)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
