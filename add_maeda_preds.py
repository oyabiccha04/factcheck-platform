import json
import os

# RIZIN 45
file_path_45 = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-45.json"
with open(file_path_45, "r", encoding="utf-8") as f:
    data_45 = json.load(f)

bout_archuleta_asakura = {
    "bout_id": "rizin45-16",
    "division": "61.0kg",
    "rules": "RIZIN MMA 5分3R",
    "red": "フアン・アーチュレッタ",
    "blue": "朝倉海",
    "outcome": {
        "winner": "朝倉海",
        "method": "TKO",
        "round": 2,
        "time": "3:20",
        "result_note": "TKO（バンタム級王座戦）"
    },
    "discipline": "MMA"
}

# Add bout if not exists
bout_exists = False
for b in data_45["cards"][0]["bouts"]:
    if "アーチュレッタ" in b.get("red", "") or "アーチュレッタ" in str(b.get("red", {})):
        bout_exists = True
        break

if not bout_exists:
    data_45["cards"][0]["bouts"].append(bout_archuleta_asakura)

maeda_pred_45 = {
    "statement_id": "stmt-rizin-45-maeda-001",
    "statement_date": "2023-12-25",
    "speaker": {
        "name": "前田日明",
        "role": "legend",
        "affiliation": "元リングス代表"
    },
    "content": {
        "raw_text": "数もらってるうちに多分ね、効いてきて動けなくなり、スピードが落ちてくると思うんですよね。今回、海が行けるんじゃないかなと思いますね。",
        "normalized_text": "持久戦になりつつも、朝倉海の必殺の攻撃力でアーチュレッタのスピードが落ち、朝倉海が勝利すると予想。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=mkkXQO7jct4",
        "timestamp": "04:58"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "前田日明",
        "source_url": "https://www.youtube.com/watch?v=mkkXQO7jct4",
        "source_ref": "stmt-rizin-45-maeda-001",
        "source_note": "YouTube勝敗予想動画から抽出",
        "expected_winner": "朝倉海",
        "expected_method": "KO",
        "target": "フアン・アーチュレッタ vs 朝倉海",
        "expected_outcome": "朝倉海の勝利（ダメージ蓄積による後半決着）",
        "deadline": "2023-12-31"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2023-12-31",
        "winner": "朝倉海",
        "method": "TKO",
        "actual_outcome": "朝倉海が2R TKO勝ち",
        "notes": "予想的中。"
    }
}
data_45.setdefault("statements", []).append(maeda_pred_45)

with open(file_path_45, "w", encoding="utf-8") as f:
    json.dump(data_45, f, indent=4, ensure_ascii=False)


# 超RIZIN 2
file_path_sr2 = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\super-rizin-2.json"
with open(file_path_sr2, "r", encoding="utf-8") as f:
    data_sr2 = json.load(f)

maeda_pred_sr2 = {
    "statement_id": "stmt-super-rizin-2-maeda-001",
    "statement_date": "2023-07-20",
    "speaker": {
        "name": "前田日明",
        "role": "legend",
        "affiliation": "元リングス代表"
    },
    "content": {
        "raw_text": "今の状態だったら7:3ですね。ケラモフが有利。",
        "normalized_text": "ケラモフの体の強さや高速タックルなどを高く評価し、現状では7:3でケラモフが有利と予想。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=8lUwXIVS-2E",
        "timestamp": "02:26"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "前田日明",
        "source_url": "https://www.youtube.com/watch?v=8lUwXIVS-2E",
        "source_ref": "stmt-super-rizin-2-maeda-001",
        "source_note": "YouTube勝敗予想動画から抽出",
        "expected_winner": "ヴガール・ケラモフ",
        "expected_method": None,
        "target": "朝倉未来 vs ヴガール・ケラモフ",
        "expected_outcome": "ヴガール・ケラモフの勝利（7:3で有利）",
        "deadline": "2023-07-30"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2023-07-30",
        "winner": "ヴガール・ケラモフ",
        "method": "Submission",
        "actual_outcome": "ヴガール・ケラモフが1R 一本勝ち",
        "notes": "予想的中。"
    }
}
data_sr2.setdefault("statements", []).append(maeda_pred_sr2)

with open(file_path_sr2, "w", encoding="utf-8") as f:
    json.dump(data_sr2, f, indent=4, ensure_ascii=False)

