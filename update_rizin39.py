import json
from datetime import datetime

file_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-39.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Retain only specific bouts
bouts_to_keep = ["rizin39-03", "rizin39-09", "rizin39-11", "rizin39-12"]
new_bouts = []
for bout in data["cards"][0]["bouts"]:
    if bout["bout_id"] in bouts_to_keep:
        new_bouts.append(bout)
data["cards"][0]["bouts"] = new_bouts

# Recreate statements
statements = []

# 1. 扇久保博正 (牛久 vs クレベル)
statements.append({
    "statement_id": "stmt-rizin-39-001",
    "statement_date": "2022-10-19",
    "speaker": {
        "name": "扇久保博正",
        "role": "fighter",
        "affiliation": "パラエストラ松戸"
    },
    "content": {
        "raw_text": "クレベル選手、腕十字一本勝ちあるんじゃないかなと",
        "normalized_text": "クレベル・コイケの腕十字による一本勝ちを予想。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "timestamp": "16:18"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "扇久保博正",
        "source_url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "source_ref": "statement_id=stmt-rizin-39-001",
        "source_note": "扇久保博正公式YouTube（勝敗予想動画）から抽出",
        "expected_winner": "クレベル・コイケ",
        "expected_method": "SUB",
        "target": "牛久絢太郎 vs クレベル・コイケ",
        "expected_outcome": "クレベル・コイケが一本勝ち（腕十字）",
        "deadline": "2022-10-23"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2022-10-23",
        "winner": "クレベル・コイケ",
        "method": "Submission",
        "actual_outcome": "クレベル・コイケが三角絞めで一本勝ち",
        "notes": "一本勝ちという予想は的中（極め手は三角絞め）。"
    }
})

# 2. ホベルト・サトシ・ソウザ (牛久 vs クレベル)
statements.append({
    "statement_id": "stmt-rizin-39-002",
    "statement_date": "2022-10-15",
    "speaker": {
        "name": "ホベルト・サトシ・ソウザ",
        "role": "fighter",
        "affiliation": "ボンサイ柔術"
    },
    "content": {
        "raw_text": "クレベルね、ベルトやっぱね、なかなかね負けなかったですからね",
        "normalized_text": "クレベル・コイケの勝利を予想（同門としての支持・強さへの信頼）。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=LYm_VDajMM8",
        "timestamp": "10:12"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "ホベルト・サトシ・ソウザ",
        "source_url": "https://www.youtube.com/watch?v=LYm_VDajMM8",
        "source_ref": "statement_id=stmt-rizin-39-002",
        "source_note": "サトシ・ソウザ公式YouTubeより抽出",
        "expected_winner": "クレベル・コイケ",
        "expected_method": "不明",
        "target": "牛久絢太郎 vs クレベル・コイケ",
        "expected_outcome": "クレベル・コイケの勝利",
        "deadline": "2022-10-23"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2022-10-23",
        "winner": "クレベル・コイケ",
        "method": "Submission",
        "actual_outcome": "クレベル・コイケが一本勝ち",
        "notes": "予想通りクレベルの勝利。"
    }
})

# 3. 扇久保博正 (手塚 vs メイマン・マメドフ)
statements.append({
    "statement_id": "stmt-rizin-39-003",
    "statement_date": "2022-10-19",
    "speaker": {
        "name": "扇久保博正",
        "role": "fighter",
        "affiliation": "パラエストラ松戸"
    },
    "content": {
        "raw_text": "手塚選手1本勝ちするんじゃないかな。ギロチンチョーク。",
        "normalized_text": "手塚基伸のギロチンチョークによる一本勝ちを予想。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "timestamp": "11:01"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "扇久保博正",
        "source_url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "source_ref": "statement_id=stmt-rizin-39-003",
        "source_note": "扇久保博正公式YouTube（勝敗予想動画）から抽出",
        "expected_winner": "手塚基伸",
        "expected_method": "SUB",
        "target": "手塚基伸 vs メイマン・マメドフ",
        "expected_outcome": "手塚基伸が一本勝ち",
        "deadline": "2022-10-23"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2022-10-23",
        "winner": "手塚基伸",
        "method": "TKO",
        "actual_outcome": "手塚基伸がTKO勝ち",
        "notes": "勝者は的中したが、決まり手はTKO（グラウンドパンチ）。"
    }
})

# 4. 扇久保博正 (武田 vs ザック・ゼイン)
statements.append({
    "statement_id": "stmt-rizin-39-004",
    "statement_date": "2022-10-19",
    "speaker": {
        "name": "扇久保博正",
        "role": "fighter",
        "affiliation": "パラエストラ松戸"
    },
    "content": {
        "raw_text": "武田選手判定勝ちじゃないでしょうか。",
        "normalized_text": "武田光司の判定勝ちを予想。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "timestamp": "14:27"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "扇久保博正",
        "source_url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "source_ref": "statement_id=stmt-rizin-39-004",
        "source_note": "扇久保博正公式YouTube（勝敗予想動画）から抽出",
        "expected_winner": "武田光司",
        "expected_method": "DEC",
        "target": "武田光司 vs ザック・ゼイン",
        "expected_outcome": "武田光司が判定勝ち",
        "deadline": "2022-10-23"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2022-10-23",
        "winner": "武田光司",
        "method": "Submission",
        "actual_outcome": "武田光司が一本勝ち（アームバー）",
        "notes": "勝者は的中したが、決まり手は一本勝ち。"
    }
})

# 5. 扇久保博正 (スダリオ vs チューカス)
statements.append({
    "statement_id": "stmt-rizin-39-005",
    "statement_date": "2022-10-19",
    "speaker": {
        "name": "扇久保博正",
        "role": "fighter",
        "affiliation": "パラエストラ松戸"
    },
    "content": {
        "raw_text": "スダリオ選手KO勝ちと予想したいと思います。",
        "normalized_text": "スダリオ剛のKO勝ちを予想。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "timestamp": "09:38"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "扇久保博正",
        "source_url": "https://www.youtube.com/watch?v=uTo51AWHARM",
        "source_ref": "statement_id=stmt-rizin-39-005",
        "source_note": "扇久保博正公式YouTube（勝敗予想動画）から抽出",
        "expected_winner": "スダリオ剛",
        "expected_method": "KO/TKO",
        "target": "スダリオ剛 vs ヤノス・チューカス",
        "expected_outcome": "スダリオ剛がKO勝ち",
        "deadline": "2022-10-23"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2022-10-23",
        "winner": "スダリオ剛",
        "method": "TKO",
        "actual_outcome": "スダリオ剛がTKO勝ち",
        "notes": "勝者および決まり手（TKO）も的中。"
    }
})

data["statements"] = statements

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON updated successfully.")
