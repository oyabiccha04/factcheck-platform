import json
import os

def update_json(file_path, keep_bout_ids, new_statements):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for card in data.get("cards", []):
        card["bouts"] = [b for b in card.get("bouts", []) if b.get("bout_id") in keep_bout_ids]
    
    data["statements"] = new_statements
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# RIZIN 45
r45_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-45.json"
r45_stmts = [
    {
        "statement_id": "stmt-rizin-45-001",
        "statement_date": "2023-12-25",
        "speaker": {
            "name": "扇久保博正",
            "role": "fighter",
            "affiliation": "パラエストラ松戸"
        },
        "content": {
            "raw_text": "堀口選手の2ラウンド、パウンドによるKO勝ち",
            "normalized_text": "堀口恭司のKO勝ちを予想。"
        },
        "source": {
            "type": "article",
            "url": "https://sportsbull.jp/p/1699998/",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "扇久保博正",
            "source_url": "https://sportsbull.jp/p/1699998/",
            "source_ref": "statement_id=stmt-rizin-45-001",
            "source_note": "スポーツブル記事より抽出",
            "expected_winner": "堀口恭司",
            "expected_method": "KO",
            "target": "堀口恭司 vs 神龍誠",
            "expected_outcome": "堀口恭司がKO勝ち",
            "deadline": "2023-12-31"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-12-31",
            "winner": "堀口恭司",
            "method": "Submission",
            "actual_outcome": "堀口恭司が一本勝ち",
            "notes": "勝者は的中したが、決まり手は一本勝ち。"
        }
    }
]
update_json(r45_path, ["rizin45-17"], r45_stmts)


# RIZIN 46
r46_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-46.json"
r46_stmts = [
    {
        "statement_id": "stmt-rizin-46-001",
        "statement_date": "2024-04-20",
        "speaker": {
            "name": "朝倉未来",
            "role": "fighter",
            "affiliation": "JAPAN TOP TEAM"
        },
        "content": {
            "raw_text": "7:3で金原有利",
            "normalized_text": "金原正徳の勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://frentopia.com/rizin46kaneharavssuzuki-yoso/",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "朝倉未来",
            "source_url": "https://frentopia.com/rizin46kaneharavssuzuki-yoso/",
            "source_ref": "statement_id=stmt-rizin-46-001",
            "source_note": "Frentopia記事より抽出",
            "expected_winner": "金原正徳",
            "expected_method": "不明",
            "target": "鈴木千裕 vs 金原正徳",
            "expected_outcome": "金原正徳が勝利",
            "deadline": "2024-04-29"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-04-29",
            "winner": "鈴木千裕",
            "method": "KO",
            "actual_outcome": "鈴木千裕がKO勝ち",
            "notes": "予想は外れ。鈴木千裕が勝利。"
        }
    }
]
update_json(r46_path, ["rizin46-10"], r46_stmts)


# RIZIN 47
r47_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-47.json"
r47_stmts = [
    {
        "statement_id": "stmt-rizin-47-001",
        "statement_date": "2024-06-01",
        "speaker": {
            "name": "ジョビン",
            "role": "youtuber",
            "affiliation": "フリー"
        },
        "content": {
            "raw_text": "セルジオペティスが要所で上回ってギリギリ判定で勝つ",
            "normalized_text": "セルジオ・ペティスの判定勝ちを予想。"
        },
        "source": {
            "type": "youtube",
            "url": "https://www.youtube.com/watch?v=1EP1EOLHwFI",
            "timestamp": "00:43:01"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ジョビン",
            "source_url": "https://www.youtube.com/watch?v=1EP1EOLHwFI",
            "source_ref": "statement_id=stmt-rizin-47-001",
            "source_note": "YouTube動画より抽出",
            "expected_winner": "セルジオ・ペティス",
            "expected_method": "DEC",
            "target": "堀口恭司 vs セルジオ・ペティス",
            "expected_outcome": "セルジオ・ペティスが判定勝ち",
            "deadline": "2024-06-09"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-06-09",
            "winner": "堀口恭司",
            "method": "Decision",
            "actual_outcome": "堀口恭司が判定勝ち",
            "notes": "予想は外れ。堀口恭司が勝利。"
        }
    },
    {
        "statement_id": "stmt-rizin-47-002",
        "statement_date": "2024-06-05",
        "speaker": {
            "name": "大沢ケンジ",
            "role": "retired fighter",
            "affiliation": "和術慧舟會HEARTS"
        },
        "content": {
            "raw_text": "堀口君の勝利",
            "normalized_text": "堀口恭司の勝利を予想。"
        },
        "source": {
            "type": "youtube",
            "url": "https://www.youtube.com/watch?v=N2-yzbRX824",
            "timestamp": "00:06:08"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "大沢ケンジ",
            "source_url": "https://www.youtube.com/watch?v=N2-yzbRX824",
            "source_ref": "statement_id=stmt-rizin-47-002",
            "source_note": "YouTube動画より抽出",
            "expected_winner": "堀口恭司",
            "expected_method": "不明",
            "target": "堀口恭司 vs セルジオ・ペティス",
            "expected_outcome": "堀口恭司が勝利",
            "deadline": "2024-06-09"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-06-09",
            "winner": "堀口恭司",
            "method": "Decision",
            "actual_outcome": "堀口恭司が判定勝ち",
            "notes": "予想的中。"
        }
    },
    {
        "statement_id": "stmt-rizin-47-003",
        "statement_date": "2024-06-07",
        "speaker": {
            "name": "スポーティングニュース",
            "role": "media",
            "affiliation": "Sporting News"
        },
        "content": {
            "raw_text": "堀口の判定勝ちを予想",
            "normalized_text": "堀口恭司の判定勝ちを予想。"
        },
        "source": {
            "type": "article",
            "url": "https://www.sportingnews.com/jp/mma/news/2024-june-9-rizin-47-horiguchi-vs-pettis-prediction-card/e2d1d7fa231b62453065344d",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "スポーティングニュース",
            "source_url": "https://www.sportingnews.com/jp/mma/news/2024-june-9-rizin-47-horiguchi-vs-pettis-prediction-card/e2d1d7fa231b62453065344d",
            "source_ref": "statement_id=stmt-rizin-47-003",
            "source_note": "Sporting News記事より抽出",
            "expected_winner": "堀口恭司",
            "expected_method": "DEC",
            "target": "堀口恭司 vs セルジオ・ペティス",
            "expected_outcome": "堀口恭司が判定勝ち",
            "deadline": "2024-06-09"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-06-09",
            "winner": "堀口恭司",
            "method": "Decision",
            "actual_outcome": "堀口恭司が判定勝ち",
            "notes": "予想的中。"
        }
    }
]
update_json(r47_path, ["rizin47-09"], r47_stmts)

print("Updated RIZIN 45, 46, 47")
