import json

file_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-39.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 6. 金原正徳 (牛久 vs クレベル)
data["statements"].append({
    "statement_id": "stmt-rizin-39-006",
    "statement_date": "2022-10-18", # Approximate date based on typical upload time
    "speaker": {
        "name": "金原正徳",
        "role": "fighter",
        "affiliation": "リバーサルジム立川ALPHA"
    },
    "content": {
        "raw_text": "俺は牛久（絢太郎）が勝っちゃうんじゃないかなと思ってるんです。フィジカル負けしないってのは多分大きいし、15分こなせる体力と心の強さはあるから。",
        "normalized_text": "牛久絢太郎の勝利を予想（フィジカルとスタミナを評価）。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=Whrxs9sjqDk",
        "timestamp": "09:55"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "金原正徳",
        "source_url": "https://www.youtube.com/watch?v=Whrxs9sjqDk",
        "source_ref": "statement_id=stmt-rizin-39-006",
        "source_note": "金原正徳公式YouTube（勝敗予想動画）から抽出",
        "expected_winner": "牛久絢太郎",
        "expected_method": "DEC",
        "target": "牛久絢太郎 vs クレベル・コイケ",
        "expected_outcome": "牛久絢太郎が勝利する（判定勝ちなど）",
        "deadline": "2022-10-23"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2022-10-23",
        "winner": "クレベル・コイケ",
        "method": "Submission",
        "actual_outcome": "クレベル・コイケが三角絞めで一本勝ち",
        "notes": "予想は外れ。クレベルが2Rで一本勝ちした。"
    }
})

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added Kanehara's prediction.")
