import json

file_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\super-rizin-2.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 削除されてしまったboutsを復元
bouts_to_restore = [
    {
        "bout_id": "super-rizin-2-bout-13",
        "bout_order": 13,
        "division": "フェザー級タイトルマッチ",
        "rules": "RIZIN MMAルール 5分5R",
        "weight_kg": 66.0,
        "discipline": "MMA",
        "red": {
            "name": "ヴガール・ケラモフ",
            "nickname": None,
            "nationality": "Azerbaijan",
            "affiliation": None
        },
        "blue": {
            "name": "朝倉未来",
            "nickname": None,
            "nationality": "Japan",
            "affiliation": "JAPAN TOP TEAM"
        },
        "outcome": {
            "winner": "ヴガール・ケラモフ",
            "method": "Submission",
            "method_detail": "リアネイキッドチョーク",
            "round": 1,
            "time": "2:41",
            "result_note": "フェザー級タイトルマッチ。「またしてもベルト奪取ならず」—朝倉は2度目の王座挑戦失敗。ケラモフが王座防衛。"
        }
    },
    {
        "bout_id": "super-rizin-2-bout-04",
        "bout_order": 4,
        "division": "フライ級タイトルマッチ",
        "rules": "Bellatorルール 5分3R",
        "weight_kg": 56.7,
        "discipline": "MMA",
        "red": {
            "name": "堀口恭司",
            "nickname": None,
            "nationality": "Japan",
            "affiliation": None
        },
        "blue": {
            "name": "神龍誠",
            "nickname": None,
            "nationality": "Japan",
            "affiliation": None
        },
        "outcome": {
            "winner": None,
            "method": "No Contest",
            "method_detail": "偶発的なサミング",
            "round": 1,
            "time": "0:25",
            "result_note": "1R25秒、偶発的なサミングによりノーコンテスト。"
        }
    }
]

data["cards"][0]["bouts"] = bouts_to_restore

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Restored bouts for super-rizin-2.json")
