import json
import os

base_dir = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events"

# --- Super RIZIN 2 ---
with open(os.path.join(base_dir, "super-rizin-2.json"), "r", encoding="utf-8") as f:
    sr2 = json.load(f)

sr2["statements"] = [
    {
        "statement_id": "stmt-super-rizin-2-001",
        "statement_date": "2023-07-09",
        "speaker": {
            "name": "金原正徳",
            "role": "fighter",
            "affiliation": "リバーサルジム立川ALPHA"
        },
        "content": {
            "raw_text": "未来が判定勝ちして、『判定あってるのか？』と話題になるまでがワンセット",
            "normalized_text": "朝倉未来の判定勝ちを予想。"
        },
        "source": {
            "type": "article",
            "url": "https://spread-sports.jp/archives/214348",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "金原正徳",
            "source_url": "https://spread-sports.jp/archives/214348",
            "source_ref": "statement_id=stmt-super-rizin-2-001",
            "source_note": "トークショー記事より抽出",
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
    },
    {
        "statement_id": "stmt-super-rizin-2-002",
        "statement_date": "2023-07-09",
        "speaker": {
            "name": "石渡伸太郎",
            "role": "retired fighter",
            "affiliation": "CAVE"
        },
        "content": {
            "raw_text": "未来選手が危なけなく勝つ。相性的に優位。",
            "normalized_text": "朝倉未来の勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://spread-sports.jp/archives/214348",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "石渡伸太郎",
            "source_url": "https://spread-sports.jp/archives/214348",
            "source_ref": "statement_id=stmt-super-rizin-2-002",
            "source_note": "トークショー記事より抽出",
            "expected_winner": "朝倉未来",
            "expected_method": "不明",
            "target": "朝倉未来 vs ヴガール・ケラモフ",
            "expected_outcome": "朝倉未来が勝利",
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
    },
    {
        "statement_id": "stmt-super-rizin-2-003",
        "statement_date": "2023-07-09",
        "speaker": {
            "name": "佐々木憂流迦",
            "role": "fighter",
            "affiliation": "セラ・ロンゴ・ファイトチーム"
        },
        "content": {
            "raw_text": "未来選手が勝つ。相性がいいと思う。",
            "normalized_text": "朝倉未来の勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://spread-sports.jp/archives/214348",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "佐々木憂流迦",
            "source_url": "https://spread-sports.jp/archives/214348",
            "source_ref": "statement_id=stmt-super-rizin-2-003",
            "source_note": "トークショー記事より抽出",
            "expected_winner": "朝倉未来",
            "expected_method": "不明",
            "target": "朝倉未来 vs ヴガール・ケラモフ",
            "expected_outcome": "朝倉未来が勝利",
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
    },
    {
        "statement_id": "stmt-super-rizin-2-004",
        "statement_date": "2023-07-28",
        "speaker": {
            "name": "パトリシオ・ピットブル",
            "role": "fighter",
            "affiliation": "ピットブル・ブラザーズ"
        },
        "content": {
            "raw_text": "多分、未来が勝つと思う。親友なので彼に挑戦する気は特にないよ",
            "normalized_text": "朝倉未来の勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://gonkaku.jp/articles/14339",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "パトリシオ・ピットブル",
            "source_url": "https://gonkaku.jp/articles/14339",
            "source_ref": "statement_id=stmt-super-rizin-2-004",
            "source_note": "ゴング格闘技の記事より抽出",
            "expected_winner": "朝倉未来",
            "expected_method": "不明",
            "target": "朝倉未来 vs ヴガール・ケラモフ",
            "expected_outcome": "朝倉未来が勝利",
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
    },
    {
        "statement_id": "stmt-super-rizin-2-005",
        "statement_date": "2023-07-09",
        "speaker": {
            "name": "石渡伸太郎",
            "role": "retired fighter",
            "affiliation": "CAVE"
        },
        "content": {
            "raw_text": "堀口恭司のワンサイド。神龍は勝つとしたらとしたらフロントチョークとか",
            "normalized_text": "堀口恭司のワンサイド勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://spread-sports.jp/archives/214346",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "石渡伸太郎",
            "source_url": "https://spread-sports.jp/archives/214346",
            "source_ref": "statement_id=stmt-super-rizin-2-005",
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
    },
    {
        "statement_id": "stmt-super-rizin-2-006",
        "statement_date": "2023-07-09",
        "speaker": {
            "name": "佐々木憂流迦",
            "role": "fighter",
            "affiliation": "セラ・ロンゴ・ファイトチーム"
        },
        "content": {
            "raw_text": "100％堀口くんが勝ちます",
            "normalized_text": "堀口恭司の勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://spread-sports.jp/archives/214346",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "佐々木憂流迦",
            "source_url": "https://spread-sports.jp/archives/214346",
            "source_ref": "statement_id=stmt-super-rizin-2-006",
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
    },
    {
        "statement_id": "stmt-super-rizin-2-007",
        "statement_date": "2023-07-22",
        "speaker": {
            "name": "朝倉未来",
            "role": "fighter",
            "affiliation": "トライフォース赤坂"
        },
        "content": {
            "raw_text": "やっぱりここは堀口選手が勝つんじゃないかと思います。3R以内にKO",
            "normalized_text": "堀口恭司の3R以内KO勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://encount.press/archives/489158/",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "朝倉未来",
            "source_url": "https://encount.press/archives/489158/",
            "source_ref": "statement_id=stmt-super-rizin-2-007",
            "source_note": "YouTube予想を伝える記事より抽出",
            "expected_winner": "堀口恭司",
            "expected_method": "KO/TKO",
            "target": "堀口恭司 vs 神龍誠",
            "expected_outcome": "堀口恭司が3R以内にKO勝ち",
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
]

bouts_sr2 = []
for bout in sr2["cards"][0]["bouts"] + sr2["cards"][1]["bouts"]:
    if "ケラモフ" in bout["red"] or "ケラモフ" in bout["blue"]:
        bouts_sr2.append(bout)
    if "堀口" in bout["red"] or "堀口" in bout["blue"]:
        bouts_sr2.append(bout)

sr2["cards"] = [{"card_id": "main", "card_name": "超RIZIN.2", "bouts": bouts_sr2}]

with open(os.path.join(base_dir, "super-rizin-2.json"), "w", encoding="utf-8") as f:
    json.dump(sr2, f, indent=4, ensure_ascii=False)


# --- RIZIN.44 ---
with open(os.path.join(base_dir, "rizin-44.json"), "r", encoding="utf-8") as f:
    r44 = json.load(f)

r44["statements"] = [
    {
        "statement_id": "stmt-rizin-44-001",
        "statement_date": "2023-09-20",
        "speaker": {
            "name": "石渡伸太郎",
            "role": "retired fighter",
            "affiliation": "CAVE"
        },
        "content": {
            "raw_text": "僕はクレベル選手の勝利です",
            "normalized_text": "クレベル・コイケの勝利を予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=saReB_anyS4",
            "timestamp": "04:53"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "石渡伸太郎",
            "source_url": "https://www.youtube.com/watch?v=saReB_anyS4",
            "source_ref": "statement_id=stmt-rizin-44-001",
            "source_note": "石渡伸太郎公式YouTubeより抽出",
            "expected_winner": "クレベル・コイケ",
            "expected_method": "不明",
            "target": "クレベル・コイケ vs 金原正徳",
            "expected_outcome": "クレベル・コイケが勝利",
            "deadline": "2023-09-24"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-09-24",
            "winner": "金原正徳",
            "method": "Decision",
            "actual_outcome": "金原正徳が判定勝ち",
            "notes": "予想は外れ。金原正徳が勝利した。"
        }
    },
    {
        "statement_id": "stmt-rizin-44-002",
        "statement_date": "2023-09-20",
        "speaker": {
            "name": "石渡伸太郎",
            "role": "retired fighter",
            "affiliation": "CAVE"
        },
        "content": {
            "raw_text": "せーの、牛久！",
            "normalized_text": "牛久絢太郎の勝利を予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=TT_VYrTccbY",
            "timestamp": "01:08"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "石渡伸太郎",
            "source_url": "https://www.youtube.com/watch?v=TT_VYrTccbY",
            "source_ref": "statement_id=stmt-rizin-44-002",
            "source_note": "石渡伸太郎公式YouTubeより抽出",
            "expected_winner": "牛久絢太郎",
            "expected_method": "不明",
            "target": "牛久絢太郎 vs 萩原京平",
            "expected_outcome": "牛久絢太郎が勝利",
            "deadline": "2023-09-24"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-09-24",
            "winner": "牛久絢太郎",
            "method": "Decision",
            "actual_outcome": "牛久絢太郎が判定勝ち",
            "notes": "予想通り牛久絢太郎が勝利した。"
        }
    }
]

bouts_r44 = []
for bout in r44["cards"][0]["bouts"]:
    if "クレベル" in bout["red"] and "金原" in bout["blue"]:
        bouts_r44.append(bout)
    if "牛久" in bout["red"] and "萩原" in bout["blue"]:
        bouts_r44.append(bout)
r44["cards"] = [{"card_id": "main", "card_name": "メインカード", "bouts": bouts_r44}]

with open(os.path.join(base_dir, "rizin-44.json"), "w", encoding="utf-8") as f:
    json.dump(r44, f, indent=4, ensure_ascii=False)


# --- RIZIN LANDMARK 7 ---
with open(os.path.join(base_dir, "rizin-landmark-7-azerbaijan.json"), "r", encoding="utf-8") as f:
    lm7 = json.load(f)

lm7["statements"] = [
    {
        "statement_id": "stmt-rizin-lm7-001",
        "statement_date": "2023-11-02",
        "speaker": {
            "name": "平本蓮",
            "role": "fighter",
            "affiliation": "剛毅會"
        },
        "content": {
            "raw_text": "ケラモフが普通に勝ちそうっすね",
            "normalized_text": "ヴガール・ケラモフの勝利を予想。"
        },
        "source": {
            "type": "article",
            "url": "https://spread-sports.jp/archives/236536",
            "timestamp": None
        },
        "prediction": {
            "exists": True,
            "predictor_name": "平本蓮",
            "source_url": "https://spread-sports.jp/archives/236536",
            "source_ref": "statement_id=stmt-rizin-lm7-001",
            "source_note": "SPREAD記事（公式YouTubeの内容をまとめた記事）より抽出",
            "expected_winner": "ヴガール・ケラモフ",
            "expected_method": "不明",
            "target": "ヴガール・ケラモフ vs 鈴木千裕",
            "expected_outcome": "ヴガール・ケラモフが勝利",
            "deadline": "2023-11-04"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-11-04",
            "winner": "鈴木千裕",
            "method": "KO",
            "actual_outcome": "鈴木千裕が1R KO勝ち",
            "notes": "予想は外れ。鈴木千裕が勝利。"
        }
    },
    {
        "statement_id": "stmt-rizin-lm7-002",
        "statement_date": "2023-11-01",
        "speaker": {
            "name": "石渡伸太郎",
            "role": "retired fighter",
            "affiliation": "CAVE"
        },
        "content": {
            "raw_text": "どっかで（鈴木の）ボロが出ちゃうんじゃないかっていう予想",
            "normalized_text": "ヴガール・ケラモフの勝利を予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=L5YE_LvFqn8",
            "timestamp": "10:42"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "石渡伸太郎",
            "source_url": "https://www.youtube.com/watch?v=L5YE_LvFqn8",
            "source_ref": "statement_id=stmt-rizin-lm7-002",
            "source_note": "石渡伸太郎公式YouTubeより抽出",
            "expected_winner": "ヴガール・ケラモフ",
            "expected_method": "不明",
            "target": "ヴガール・ケラモフ vs 鈴木千裕",
            "expected_outcome": "ヴガール・ケラモフが勝利",
            "deadline": "2023-11-04"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2023-11-04",
            "winner": "鈴木千裕",
            "method": "KO",
            "actual_outcome": "鈴木千裕が1R KO勝ち",
            "notes": "予想は外れ。鈴木千裕が勝利。"
        }
    }
]

bouts_lm7 = []
for bout in lm7["cards"][0]["bouts"]:
    if "ケラモフ" in bout["red"] and "鈴木" in bout["blue"]:
        bouts_lm7.append(bout)
lm7["cards"] = [{"card_id": "main", "card_name": "メインカード", "bouts": bouts_lm7}]

with open(os.path.join(base_dir, "rizin-landmark-7-azerbaijan.json"), "w", encoding="utf-8") as f:
    json.dump(lm7, f, indent=4, ensure_ascii=False)

print("Updated Super RIZIN 2, RIZIN 44, RIZIN Landmark 7")
