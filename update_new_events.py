import json

def update_ufc_file(file_path, target_bout_id):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for card in data.get("cards", []):
        card["bouts"] = [b for b in card.get("bouts", []) if b.get("bout_id") == target_bout_id]
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_rizin49_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Keep specific bouts
    valid_bouts = ["rizin49-10", "rizin49-12", "rizin49-14"]
    for card in data.get("cards", []):
        card["bouts"] = [b for b in card.get("bouts", []) if b.get("bout_id") in valid_bouts]
        
    # Replace statements entirely because the old ones are fake
    new_statements = [
        {
            "statement_id": "stmt-rizin-49-new-001",
            "statement_date": "2024-12-25",
            "speaker": {
                "name": "ジョビン",
                "role": "youtuber",
                "affiliation": "格闘技YouTuber・元DEEPフェザー級王者"
            },
            "content": {
                "raw_text": "フィニッシュするなケラモフが3ラウンド",
                "normalized_text": "ケラモフが3ラウンドでフィニッシュ勝利すると予想"
            },
            "source": {
                "type": "video",
                "url": "https://www.youtube.com/watch?v=as_ot9pNXIs",
                "timestamp": "20:19"
            },
            "prediction": {
                "exists": True,
                "predictor_name": "ジョビン",
                "source_url": "https://www.youtube.com/watch?v=as_ot9pNXIs",
                "source_ref": "stmt-rizin-49-new-001",
                "source_note": "YouTube勝敗予想動画から抽出",
                "expected_winner": "ヴガール・ケラモフ",
                "expected_method": "Finish",
                "target": "ホベルト・サトシ・ソウザ vs ヴガール・ケラモフ",
                "expected_outcome": "ケラモフが3Rにフィニッシュ勝利",
                "deadline": "2024-12-31"
            },
            "verification": {
                "status": "resolved",
                "verification_date": "2025-01-01",
                "winner": "ホベルト・サトシ・ソウザ",
                "method": "Submission",
                "actual_outcome": "サトシが1R 4:45で三角絞めで一本勝ち",
                "notes": "予想外れ。サトシが1Rで一本勝ち。"
            }
        },
        {
            "statement_id": "stmt-rizin-49-new-002",
            "statement_date": "2024-12-25",
            "speaker": {
                "name": "ジョビン",
                "role": "youtuber",
                "affiliation": "格闘技YouTuber・元DEEPフェザー級王者"
            },
            "content": {
                "raw_text": "ここズバリえ鈴木色の慶王勝ち予想にして",
                "normalized_text": "鈴木千裕のKO勝ちを予想"
            },
            "source": {
                "type": "video",
                "url": "https://www.youtube.com/watch?v=as_ot9pNXIs",
                "timestamp": "28:10"
            },
            "prediction": {
                "exists": True,
                "predictor_name": "ジョビン",
                "source_url": "https://www.youtube.com/watch?v=as_ot9pNXIs",
                "source_ref": "stmt-rizin-49-new-002",
                "source_note": "YouTube勝敗予想動画から抽出",
                "expected_winner": "鈴木千裕",
                "expected_method": "KO",
                "target": "鈴木千裕 vs クレベル・コイケ",
                "expected_outcome": "鈴木千裕がKO勝利",
                "deadline": "2024-12-31"
            },
            "verification": {
                "status": "resolved",
                "verification_date": "2025-01-01",
                "winner": "クレベル・コイケ",
                "method": "Decision",
                "actual_outcome": "クレベルが判定3-0で勝利",
                "notes": "予想外れ。クレベルが判定勝利。"
            }
        },
        {
            "statement_id": "stmt-rizin-49-new-003",
            "statement_date": "2024-12-28",
            "speaker": {
                "name": "石渡伸太郎",
                "role": "coach",
                "affiliation": "CAVE"
            },
            "content": {
                "raw_text": "僕はサト選手と思います1本がち良そうすか1本取ります",
                "normalized_text": "サトシが一本勝ちすると予想"
            },
            "source": {
                "type": "video",
                "url": "https://www.youtube.com/watch?v=dDDq7hGWscE",
                "timestamp": "07:45"
            },
            "prediction": {
                "exists": True,
                "predictor_name": "石渡伸太郎",
                "source_url": "https://www.youtube.com/watch?v=dDDq7hGWscE",
                "source_ref": "stmt-rizin-49-new-003",
                "source_note": "YouTube勝敗予想動画から抽出",
                "expected_winner": "ホベルト・サトシ・ソウザ",
                "expected_method": "Submission",
                "target": "ホベルト・サトシ・ソウザ vs ヴガール・ケラモフ",
                "expected_outcome": "サトシが一本勝ち",
                "deadline": "2024-12-31"
            },
            "verification": {
                "status": "resolved",
                "verification_date": "2025-01-01",
                "winner": "ホベルト・サトシ・ソウザ",
                "method": "Submission",
                "actual_outcome": "サトシが1R 4:45で三角絞めで一本勝ち",
                "notes": "予想的中。"
            }
        },
        {
            "statement_id": "stmt-rizin-49-new-004",
            "statement_date": "2024-12-28",
            "speaker": {
                "name": "石渡伸太郎",
                "role": "coach",
                "affiliation": "CAVE"
            },
            "content": {
                "raw_text": "せーの 元 お全員元谷全員元屋選手",
                "normalized_text": "元谷友貴の勝利を予想"
            },
            "source": {
                "type": "video",
                "url": "https://www.youtube.com/watch?v=qKHHCjT2Oac",
                "timestamp": "02:10"
            },
            "prediction": {
                "exists": True,
                "predictor_name": "石渡伸太郎",
                "source_url": "https://www.youtube.com/watch?v=qKHHCjT2Oac",
                "source_ref": "stmt-rizin-49-new-004",
                "source_note": "YouTube勝敗予想動画から抽出",
                "expected_winner": "元谷友貴",
                "expected_method": None,
                "target": "元谷友貴 vs 秋元強真",
                "expected_outcome": "元谷友貴が勝利",
                "deadline": "2024-12-31"
            },
            "verification": {
                "status": "resolved",
                "verification_date": "2025-01-01",
                "winner": "元谷友貴",
                "method": "Decision",
                "actual_outcome": "元谷が判定3-0で勝利",
                "notes": "予想的中。"
            }
        }
    ]
    data["statements"] = new_statements
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# Main execution
ufc311_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\ufc-311.json"
ufc310_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\ufc-310.json"
ufc244_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\ufc-fight-night-244.json"
rizin49_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-49.json"

update_ufc_file(ufc311_path, "ufc-311-001")
update_ufc_file(ufc310_path, "ufc-310-001")
update_ufc_file(ufc244_path, "ufc-fight-night-244-001")
update_rizin49_file(rizin49_path)

print("Updated 4 events successfully!")
