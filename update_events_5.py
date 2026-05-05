import json
import os

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def clean_bouts(filepath):
    data = load_json(filepath)
    predicted_targets = set()
    for stmt in data.get("statements", []):
        if stmt.get("prediction", {}).get("exists", False):
            predicted_targets.add(stmt["prediction"]["target"])
            
    # keep bouts where red name or blue name is in any target string
    for card in data.get("cards", []):
        bouts_to_keep = []
        for bout in card.get("bouts", []):
            red_name = bout.get("red", {}).get("name", "") if isinstance(bout.get("red"), dict) else bout.get("red", "")
            blue_name = bout.get("blue", {}).get("name", "") if isinstance(bout.get("blue"), dict) else bout.get("blue", "")
            
            keep = False
            for target in predicted_targets:
                if red_name and red_name in target:
                    keep = True
                if blue_name and blue_name in target:
                    keep = True
            
            if keep:
                bouts_to_keep.append(bout)
        card["bouts"] = bouts_to_keep
    
    save_json(filepath, data)


# 1. RIZIN LANDMARK 13
clean_bouts(r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-landmark-13-fukuoka.json")

# 2. RIZIN 52
clean_bouts(r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-52.json")

# 3. UFC Fight Night: Bautista vs. Oliveira (LV113)
# Add Jobin prediction
lv113_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\ufc-fight-night-lv113.json"
lv113_data = load_json(lv113_path)

jobin_pred = {
    "statement_id": "stmt-ufc-lv113-jobin-001",
    "statement_date": "2026-02-05",
    "speaker": {
        "name": "ジョビン",
        "role": "analyst",
        "affiliation": "YouTuber・元総合格闘家"
    },
    "content": {
        "raw_text": "アルバジもうカーフ効かしフィニッシュも全然あり得ると思うな。ここは堀口勝ってほしい。ま、勝つと思うし買ったらマジ面白くなる。",
        "normalized_text": "堀口恭司が勝利すると予想。アルバジの強さを認めつつも、堀口のカーフキックからのフィニッシュもあり得ると分析。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=3fpw7fOYXpU",
        "timestamp": "0:45"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "ジョビン",
        "source_url": "https://www.youtube.com/watch?v=3fpw7fOYXpU",
        "source_ref": "stmt-ufc-lv113-jobin-001",
        "source_note": "YouTube自動字幕より抽出（確認日：2026-05-05）。",
        "expected_winner": "堀口恭司",
        "expected_method": None,
        "target": "堀口恭司 vs アミル・アルバジ",
        "expected_outcome": "堀口恭司が勝利",
        "deadline": "2026-02-07"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2026-02-08",
        "winner": "堀口恭司",
        "method": "Decision",
        "actual_outcome": "堀口が全会一致判定で勝利。",
        "notes": "予想的中。"
    }
}

stmt_exists = any(s["statement_id"] == "stmt-ufc-lv113-jobin-001" for s in lv113_data["statements"])
if not stmt_exists:
    lv113_data["statements"].append(jobin_pred)
save_json(lv113_path, lv113_data)
clean_bouts(lv113_path)

# 4. RIZIN師走の超強者祭り
clean_bouts(r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-shiwasu-2025.json")

# 5. UFC Fight Night: Qatar 2025
clean_bouts(r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\ufc-fight-night-qatar-2025.json")

print("Done")
