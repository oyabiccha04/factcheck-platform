import json

file_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\super-rizin-2.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 新しい予想を追加
# 1. 大沢ケンジ (朝倉未来 vs ヴガール・ケラモフ)
new_pred_1 = {
    "statement_id": "stmt-super-rizin-2-008",
    "statement_date": "2023-07-16",
    "speaker": {
        "name": "大沢ケンジ",
        "role": "retired fighter",
        "affiliation": "和術慧舟會HEARTS"
    },
    "content": {
        "raw_text": "朝倉未来の判定勝利で",
        "normalized_text": "朝倉未来の判定勝ちを予想。"
    },
    "source": {
        "type": "youtube",
        "url": "https://www.youtube.com/watch?v=gs5JOs8w0kM",
        "timestamp": "00:14:07"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "大沢ケンジ",
        "source_url": "https://www.youtube.com/watch?v=gs5JOs8w0kM",
        "source_ref": "statement_id=stmt-super-rizin-2-008",
        "source_note": "YouTube動画より抽出",
        "expected_winner": "朝倉未来",
        "expected_method": "DEC",
        "target": "朝倉未来 vs ヴガール・ケラモフ",
        "expected_outcome": "朝倉未来が判定勝ち",
        "deadline": "2023-07-30"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2023-07-30",
        "winner": "ヴガール・ケラモフ",
        "method": "Submission",
        "actual_outcome": "ヴガール・ケラモフが一本勝ち",
        "notes": "予想は外れ。"
    }
}

# 2. 大沢ケンジ (堀口恭司 vs 神龍誠)
new_pred_2 = {
    "statement_id": "stmt-super-rizin-2-009",
    "statement_date": "2023-07-16",
    "speaker": {
        "name": "大沢ケンジ",
        "role": "retired fighter",
        "affiliation": "和術慧舟會HEARTS"
    },
    "content": {
        "raw_text": "堀口君勝利なの予想ですよね",
        "normalized_text": "堀口恭司の勝利を予想。"
    },
    "source": {
        "type": "youtube",
        "url": "https://www.youtube.com/watch?v=gs5JOs8w0kM",
        "timestamp": "00:18:14"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "大沢ケンジ",
        "source_url": "https://www.youtube.com/watch?v=gs5JOs8w0kM",
        "source_ref": "statement_id=stmt-super-rizin-2-009",
        "source_note": "YouTube動画より抽出",
        "expected_winner": "堀口恭司",
        "expected_method": "不明",
        "target": "堀口恭司 vs 神龍誠",
        "expected_outcome": "堀口恭司が勝利",
        "deadline": "2023-07-30"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2023-07-30",
        "winner": "ノーコンテスト",
        "method": "NC",
        "actual_outcome": "ノーコンテスト（アイポークにより）",
        "notes": "アイポークのためノーコンテストとなった。"
    }
}

# 3. 金原正徳 (堀口恭司 vs 神龍誠)
new_pred_3 = {
    "statement_id": "stmt-super-rizin-2-010",
    "statement_date": "2023-07-09",
    "speaker": {
        "name": "金原正徳",
        "role": "fighter",
        "affiliation": "リバーサルジム立川ALPHA"
    },
    "content": {
        "raw_text": "堀口勝率50%",
        "normalized_text": "堀口恭司の勝利を予想。"
    },
    "source": {
        "type": "article",
        "url": "https://spread-sports.jp/archives/214346",
        "timestamp": None
    },
    "prediction": {
        "exists": True,
        "predictor_name": "金原正徳",
        "source_url": "https://spread-sports.jp/archives/214346",
        "source_ref": "statement_id=stmt-super-rizin-2-010",
        "source_note": "トークショー記事より抽出",
        "expected_winner": "堀口恭司",
        "expected_method": "不明",
        "target": "堀口恭司 vs 神龍誠",
        "expected_outcome": "堀口恭司が勝利",
        "deadline": "2023-07-30"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2023-07-30",
        "winner": "ノーコンテスト",
        "method": "NC",
        "actual_outcome": "ノーコンテスト（アイポークにより）",
        "notes": "アイポークのためノーコンテストとなった。"
    }
}

data["statements"].extend([new_pred_1, new_pred_2, new_pred_3])

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added new predictions to super-rizin-2.json")
