import json

file_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-landmark-7-azerbaijan.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 削除されてしまったboutsを復元
bouts_to_restore = [
    {
        "bout_id": "rizin-landmark-7-az-bout-10",
        "bout_order": 10,
        "division": "フェザー級タイトルマッチ",
        "rules": "RIZIN MMAルール 5分5R",
        "weight_kg": 66.0,
        "discipline": "MMA",
        "red": {
            "name": "鈴木千裕",
            "nickname": None,
            "nationality": "Japan",
            "affiliation": None
        },
        "blue": {
            "name": "ヴガール・ケラモフ",
            "nickname": None,
            "nationality": "Azerbaijan",
            "affiliation": None
        },
        "outcome": {
            "winner": "鈴木千裕",
            "method": "KO",
            "method_detail": "アップキック→グラウンドパンチ",
            "round": 1,
            "time": "1:18",
            "result_note": "フェザー級タイトルマッチ。鈴木がバックに倒れた状態からアップキックでケラモフをぐらつかせ、グラウンドパンチを連打してレフリーストップ。鈴木千裕が第5代RIZINフェザー級王者に。"
        }
    }
]

data["cards"][0]["bouts"] = bouts_to_restore

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Restored bouts for rizin-landmark-7-azerbaijan.json")
