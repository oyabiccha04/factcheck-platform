import json

filepath = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-landmark-13-fukuoka.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Update the Jobin statement to Ougikubo
for stmt in data.get("statements", []):
    if stmt["statement_id"] == "stmt-lm13-jobin":
        stmt["statement_id"] = "stmt-lm13-ougikubo"
        stmt["speaker"] = {
            "name": "扇久保博正",
            "role": "fighter",
            "affiliation": "パラエストラ松戸"
        }
        stmt["source"]["url"] = "https://www.youtube.com/watch?v=yaSKtzqyJ9U"
        stmt["prediction"]["predictor_name"] = "扇久保博正"
        stmt["prediction"]["source_url"] = "https://www.youtube.com/watch?v=yaSKtzqyJ9U"
        break

# 2. Add Asakura Mikuru
new_preds = [
    {
        "statement_id": "stmt-lm13-asakura",
        "statement_date": "2026-03-05",
        "speaker": {
            "name": "朝倉未来",
            "role": "promoter",
            "affiliation": "JTT / 元格闘家"
        },
        "content": {
            "raw_text": "まあ、シェイドゥラエフに勝てるやつはいないと思いますね。その下で争うんじゃないですか",
            "normalized_text": "シェイドゥラエフに勝てる選手はいないと高く評価し、圧倒的勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://www.sanspo.com/article/20260305-FHKPAJTRSRGBFBLNXSXHBCEYHA/",
            "timestamp": "2026-03-05"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "朝倉未来",
            "source_url": "https://www.sanspo.com/article/20260305-FHKPAJTRSRGBFBLNXSXHBCEYHA/",
            "source_ref": "stmt-lm13-asakura",
            "source_note": "サンスポ記事より抽出（確認日：2026-05-05）。",
            "expected_winner": "ラジャブアリ・シェイドゥラエフ",
            "expected_method": None,
            "target": "ラジャブアリ・シェイドゥラエフ vs 久保優太",
            "expected_outcome": "シェイドゥラエフが勝利",
            "deadline": "2026-04-12"
        },
        "verification": {
            "status": "pending",
            "verification_date": None,
            "winner": None,
            "method": None,
            "actual_outcome": "未開催（予定）",
            "notes": None
        }
    },
    {
        "statement_id": "stmt-lm13-sonos",
        "statement_date": "2026-04-10",
        "speaker": {
            "name": "Sonos好きのブログ",
            "role": "analyst",
            "affiliation": "格闘技ブロガー"
        },
        "content": {
            "raw_text": "普通に考えればシェイドゥラエフ有利です。最終的には王者が捕まえると見ています。私の予想は、シェイドゥラエフの2R一本勝ちです。",
            "normalized_text": "久保が距離を取って戦うものの、最終的にはシェイドゥラエフが捕まえて2R一本勝ちを収めると予想。"
        },
        "source": {
            "type": "article",
            "url": "https://today-is-the-first-day.com/sonosuki/rizin-landmark-13",
            "timestamp": "試合前"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "Sonos好きのブログ",
            "source_url": "https://today-is-the-first-day.com/sonosuki/rizin-landmark-13",
            "source_ref": "stmt-lm13-sonos",
            "source_note": "ブログ記事より抽出（確認日：2026-05-05）。",
            "expected_winner": "ラジャブアリ・シェイドゥラエフ",
            "expected_method": "SUB",
            "target": "ラジャブアリ・シェイドゥラエフ vs 久保優太",
            "expected_outcome": "シェイドゥラエフの2R一本勝ち",
            "deadline": "2026-04-12"
        },
        "verification": {
            "status": "pending",
            "verification_date": None,
            "winner": None,
            "method": None,
            "actual_outcome": "未開催（予定）",
            "notes": None
        }
    }
]

existing_ids = {s["statement_id"] for s in data.get("statements", [])}
for p in new_preds:
    if p["statement_id"] not in existing_ids:
        data["statements"].append(p)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Updated RIZIN LANDMARK 13 with Asakura and others")
