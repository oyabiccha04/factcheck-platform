import json

with open("data/events/rizin-38.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_statement = {
    "statement_id": "stmt-rizin-38-004",
    "statement_date": "2022-06-25",
    "speaker": {
        "name": "内藤大助",
        "role": "retired fighter",
        "affiliation": "元WBC世界フライ級王者"
    },
    "content": {
        "raw_text": "勝つのは99%ない。キックボクサーがボクシングルールで勝てるわけない。",
        "normalized_text": "ボクシングルールでのメイウェザー勝利を予想。"
    },
    "source": {
        "type": "video",
        "url": "https://www.youtube.com/watch?v=9tN_sQqL1OM",
        "timestamp": "04:00"
    },
    "prediction": {
        "exists": True,
        "predictor_name": "内藤大助",
        "source_url": "https://www.youtube.com/watch?v=9tN_sQqL1OM",
        "source_ref": "statement_id=stmt-rizin-38-004",
        "source_note": "本人の公式YouTubeチャンネル動画より抽出",
        "expected_winner": "フロイド・メイウェザー",
        "expected_method": "不明",
        "target": "フロイド・メイウェザー vs 朝倉未来",
        "expected_outcome": "メイウェザーが勝利",
        "deadline": "2022-09-25"
    },
    "verification": {
        "status": "resolved",
        "verification_date": "2022-09-25",
        "winner": "フロイド・メイウェザー",
        "method": "TKO",
        "actual_outcome": "フロイド・メイウェザーがTKO勝ち",
        "notes": "興行クローズ後の試合結果（cards[].bouts[].outcome）に基づく"
    }
}

data["statements"].append(new_statement)

with open("data/events/rizin-38.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
