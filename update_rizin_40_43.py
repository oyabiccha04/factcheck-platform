import json
import os

files_to_process = ["rizin-40.json", "rizin-41.json", "rizin-42.json", "rizin-43.json"]
base_dir = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events"

# --- RIZIN.40 ---
with open(os.path.join(base_dir, "rizin-40.json"), "r", encoding="utf-8") as f:
    d40 = json.load(f)

d40["statements"] = [
    {
        "statement_id": "stmt-rizin-40-001",
        "statement_date": "2022-12-25",
        "speaker": {
            "name": "平本蓮",
            "role": "fighter",
            "affiliation": "剛毅會"
        },
        "content": {
            "raw_text": "（AJマッキーについて）次こそは…という形で準備を整えてくる。サトシよりクレベルが善戦する",
            "normalized_text": "AJ・マッキーの勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://www.tokyo-sports.co.jp/articles/-/249751",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "平本蓮",
            "source_url": "https://www.tokyo-sports.co.jp/articles/-/249751",
            "source_ref": "statement_id=stmt-rizin-40-001",
            "source_note": "東スポWEBの記事（平本蓮の勝敗予想インタビュー）より抽出",
            "expected_winner": "AJ・マッキー",
            "expected_method": "不明",
            "target": "ホベルト・サトシ・ソウザ vs AJ・マッキー",
            "expected_outcome": "AJ・マッキーの勝利",
            "deadline": "2022-12-31"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2022-12-31",
            "winner": "AJ・マッキー",
            "method": "Decision",
            "actual_outcome": "AJ・マッキーが判定勝ち",
            "notes": "予想通りAJ・マッキーが勝利。"
        }
    },
    {
        "statement_id": "stmt-rizin-40-002",
        "statement_date": "2022-12-25",
        "speaker": {
            "name": "平本蓮",
            "role": "fighter",
            "affiliation": "剛毅會"
        },
        "content": {
            "raw_text": "逆にサトシよりクレベルが善戦しそう",
            "normalized_text": "クレベル・コイケの勝利（または善戦）を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://www.tokyo-sports.co.jp/articles/-/249751",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "平本蓮",
            "source_url": "https://www.tokyo-sports.co.jp/articles/-/249751",
            "source_ref": "statement_id=stmt-rizin-40-002",
            "source_note": "東スポWEBの記事（平本蓮の勝敗予想インタビュー）より抽出",
            "expected_winner": "クレベル・コイケ",
            "expected_method": "不明",
            "target": "クレベル・コイケ vs パトリシオ・ピットブル",
            "expected_outcome": "クレベル・コイケの勝利",
            "deadline": "2022-12-31"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2022-12-31",
            "winner": "パトリシオ・ピットブル",
            "method": "Decision",
            "actual_outcome": "パトリシオ・ピットブルが判定勝ち",
            "notes": "予想は外れ。パトリシオが勝利。"
        }
    }
]

bouts_to_keep_40 = ["ホベルト・サトシ・ソウザ vs AJ・マッキー", "クレベル・コイケ vs パトリシオ・ピットブル"]
new_bouts_40 = []
for bout in d40["cards"][0]["bouts"]:
    target = bout["red"] + " vs " + bout["blue"]
    # Handle the fact that some JSONs might use middle dots instead of spaces
    if "サトシ" in bout["red"] and "マッキー" in bout["blue"]:
        new_bouts_40.append(bout)
    if "クレベル" in bout["red"] and "パトリシオ" in bout["blue"]:
        new_bouts_40.append(bout)
d40["cards"][0]["bouts"] = new_bouts_40

with open(os.path.join(base_dir, "rizin-40.json"), "w", encoding="utf-8") as f:
    json.dump(d40, f, indent=4, ensure_ascii=False)


# --- RIZIN.41 ---
with open(os.path.join(base_dir, "rizin-41.json"), "r", encoding="utf-8") as f:
    d41 = json.load(f)

d41["statements"] = [
    {
        "statement_id": "stmt-rizin-41-001",
        "statement_date": "2023-03-30",
        "speaker": {
            "name": "石渡伸太郎",
            "role": "retired fighter",
            "affiliation": "CAVE"
        },
        "content": {
            "raw_text": "これは僕も皇治選手予想です。芦澤選手が打ち合う展開になって飲み込まれちゃうんじゃないかなと思う",
            "normalized_text": "皇治の勝利を予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=FmZZU2y4AM8",
            "timestamp": "18:12"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "石渡伸太郎",
            "source_url": "https://www.youtube.com/watch?v=FmZZU2y4AM8",
            "source_ref": "statement_id=stmt-rizin-41-001",
            "source_note": "石渡伸太郎公式YouTubeより抽出",
            "expected_winner": "皇治",
            "expected_method": "不明",
            "target": "皇治 vs 芦澤竜誠",
            "expected_outcome": "皇治が勝利",
            "deadline": "2023-04-01"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-04-01",
            "winner": "芦澤竜誠",
            "method": "Decision",
            "actual_outcome": "芦澤竜誠が判定勝ち",
            "notes": "予想は外れ。芦澤が判定勝ち。"
        }
    }
]

new_bouts_41 = []
for bout in d41["cards"][0]["bouts"]:
    if "皇治" in bout["red"] and "芦澤" in bout["blue"]:
        new_bouts_41.append(bout)
d41["cards"][0]["bouts"] = new_bouts_41

with open(os.path.join(base_dir, "rizin-41.json"), "w", encoding="utf-8") as f:
    json.dump(d41, f, indent=4, ensure_ascii=False)


# --- RIZIN.42 ---
with open(os.path.join(base_dir, "rizin-42.json"), "r", encoding="utf-8") as f:
    d42 = json.load(f)

d42["statements"] = [
    {
        "statement_id": "stmt-rizin-42-001",
        "statement_date": "2023-05-02",
        "speaker": {
            "name": "ジョビン",
            "role": "retired fighter",
            "affiliation": "フリー"
        },
        "content": {
            "raw_text": "僕はここはアーチュレッタの判定勝ち予想にしておきます。",
            "normalized_text": "フアン・アーチュレッタの判定勝ちを予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=ewrYzHeddkE",
            "timestamp": "26:05"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ジョビン",
            "source_url": "https://www.youtube.com/watch?v=ewrYzHeddkE",
            "source_ref": "statement_id=stmt-rizin-42-001",
            "source_note": "ジョビンチャンネルより抽出",
            "expected_winner": "フアン・アーチュレッタ",
            "expected_method": "DEC",
            "target": "井上直樹 vs フアン・アーチュレッタ",
            "expected_outcome": "フアン・アーチュレッタが判定勝ち",
            "deadline": "2023-05-06"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-05-06",
            "winner": "フアン・アーチュレッタ",
            "method": "Decision",
            "actual_outcome": "フアン・アーチュレッタが判定勝ち",
            "notes": "勝者および決まり手ともに的中。"
        }
    },
    {
        "statement_id": "stmt-rizin-42-002",
        "statement_date": "2023-05-02",
        "speaker": {
            "name": "ジョビン",
            "role": "retired fighter",
            "affiliation": "フリー"
        },
        "content": {
            "raw_text": "俺は判定勝ち予想かな、朝倉海がタックル切って...判定勝ち。",
            "normalized_text": "朝倉海の判定勝ちを予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=ewrYzHeddkE",
            "timestamp": "26:48"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ジョビン",
            "source_url": "https://www.youtube.com/watch?v=ewrYzHeddkE",
            "source_ref": "statement_id=stmt-rizin-42-002",
            "source_note": "ジョビンチャンネルより抽出",
            "expected_winner": "朝倉海",
            "expected_method": "DEC",
            "target": "朝倉海 vs 元谷友貴",
            "expected_outcome": "朝倉海が判定勝ち",
            "deadline": "2023-05-06"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-05-06",
            "winner": "朝倉海",
            "method": "KO",
            "actual_outcome": "朝倉海がTKO勝ち（グラウンドの膝蹴り）",
            "notes": "勝者は的中したが、判定ではなくTKO勝ちだった。"
        }
    }
]

new_bouts_42 = []
for bout in d42["cards"][0]["bouts"]:
    if "井上" in bout["red"] and "アーチュレッタ" in bout["blue"]:
        new_bouts_42.append(bout)
    if "朝倉" in bout["red"] and "元谷" in bout["blue"]:
        new_bouts_42.append(bout)
d42["cards"][0]["bouts"] = new_bouts_42

with open(os.path.join(base_dir, "rizin-42.json"), "w", encoding="utf-8") as f:
    json.dump(d42, f, indent=4, ensure_ascii=False)


# --- RIZIN.43 ---
with open(os.path.join(base_dir, "rizin-43.json"), "r", encoding="utf-8") as f:
    d43 = json.load(f)

d43["statements"] = [
    {
        "statement_id": "stmt-rizin-43-001",
        "statement_date": "2023-06-23",
        "speaker": {
            "name": "矢地祐介",
            "role": "fighter",
            "affiliation": "フリー"
        },
        "content": {
            "raw_text": "鈴木選手が勝つんじゃないかな。1ラウンドKO勝ち予想します。",
            "normalized_text": "鈴木千裕の1R KO勝ちを予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=hWFzpHc2rVk",
            "timestamp": "07:54"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "矢地祐介",
            "source_url": "https://www.youtube.com/watch?v=hWFzpHc2rVk",
            "source_ref": "statement_id=stmt-rizin-43-001",
            "source_note": "矢地祐介公式YouTubeより抽出",
            "expected_winner": "鈴木千裕",
            "expected_method": "KO/TKO",
            "target": "クレベル・コイケ vs 鈴木千裕",
            "expected_outcome": "鈴木千裕が1R KO勝ち",
            "deadline": "2023-06-24"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-06-24",
            "winner": "ノーコンテスト",
            "method": "NC",
            "actual_outcome": "ノーコンテスト",
            "notes": "クレベルの体重超過により、試合結果はノーコンテストとなった（試合自体はクレベルの一本勝ち）。"
        }
    },
    {
        "statement_id": "stmt-rizin-43-002",
        "statement_date": "2023-06-22",
        "speaker": {
            "name": "ホベルト・サトシ・ソウザ",
            "role": "fighter",
            "affiliation": "ボンサイ柔術"
        },
        "content": {
            "raw_text": "ここはじゃあクレベル選手が勝ちます。グランドで極めもできるし。",
            "normalized_text": "クレベル・コイケの勝利（極め）を予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=hh7Z3FH31lk",
            "timestamp": "09:30"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ホベルト・サトシ・ソウザ",
            "source_url": "https://www.youtube.com/watch?v=hh7Z3FH31lk",
            "source_ref": "statement_id=stmt-rizin-43-002",
            "source_note": "ホベルト・サトシ・ソウザ公式YouTubeより抽出",
            "expected_winner": "クレベル・コイケ",
            "expected_method": "SUB",
            "target": "クレベル・コイケ vs 鈴木千裕",
            "expected_outcome": "クレベル・コイケが勝利",
            "deadline": "2023-06-24"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-06-24",
            "winner": "ノーコンテスト",
            "method": "NC",
            "actual_outcome": "ノーコンテスト",
            "notes": "試合結果はノーコンテスト。"
        }
    }
]

new_bouts_43 = []
for bout in d43["cards"][0]["bouts"]:
    if "クレベル" in bout["red"] and "鈴木" in bout["blue"]:
        new_bouts_43.append(bout)
d43["cards"][0]["bouts"] = new_bouts_43

with open(os.path.join(base_dir, "rizin-43.json"), "w", encoding="utf-8") as f:
    json.dump(d43, f, indent=4, ensure_ascii=False)

print("Processing complete.")
