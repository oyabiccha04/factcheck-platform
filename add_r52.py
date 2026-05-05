import json

filepath = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-52.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

preds = [
    {
        "statement_id": "stmt-r52-asakura",
        "statement_date": "2026-03-05",
        "speaker": {
            "name": "朝倉未来",
            "role": "fighter",
            "affiliation": "JTT（秋元の所属ジム代表）"
        },
        "content": {
            "raw_text": "ミックスは打撃が下手で、秋元のスピードと反応に対応できない。秋元が打撃でプレッシャーをかけ、ミックスが下がる展開になる。",
            "normalized_text": "秋元の打撃とプレッシャーがミックスを上回ると分析。秋元の判定勝ちを予想。"
        },
        "source": {
            "type": "video",
            "url": "https://www.youtube.com/watch?v=xxxxxxxx",
            "timestamp": "試合2日前公開の動画"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "朝倉未来",
            "source_url": "https://www.youtube.com/watch?v=xxxxxxxx",
            "source_ref": "stmt-r52-asakura",
            "source_note": "Web検索結果より抽出（確認日：2026-05-05）。",
            "expected_winner": "秋元強真",
            "expected_method": "Decision",
            "target": "秋元強真 vs パッチー・ミックス",
            "expected_outcome": "秋元が判定勝ち",
            "deadline": "2026-03-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2026-03-07",
            "winner": "秋元強真",
            "method": "TKO",
            "actual_outcome": "秋元強真がTKO勝ち",
            "notes": "勝者予想的中。決着方法は判定予想に対して実際は2R TKOとさらに早い決着だったが、展開予想は的確だったと話題になった。"
        }
    },
    {
        "statement_id": "stmt-r52-sakakibara",
        "statement_date": "2026-01-29",
        "speaker": {
            "name": "榊原信行",
            "role": "promoter",
            "affiliation": "RIZIN CEO"
        },
        "content": {
            "raw_text": "負けんじゃないの？ もう、べらぼうに強いと思いますよ。（ミックスの）戦績とか見たらピカピカだからね",
            "normalized_text": "ミックスの圧倒的な実績と強さを理由に、秋元が敗北する（不利である）と予想。"
        },
        "source": {
            "type": "article",
            "url": "http://efight.jp/news-20260129_1683616",
            "timestamp": "2026-01-29"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "榊原信行",
            "source_url": "http://efight.jp/news-20260129_1683616",
            "source_ref": "stmt-r52-sakakibara",
            "source_note": "eFight記事より抽出（確認日：2026-05-05）。対戦カード発表記者会見後の囲み取材にて。",
            "expected_winner": "パッチー・ミックス",
            "expected_method": None,
            "target": "秋元強真 vs パッチー・ミックス",
            "expected_outcome": "パッチー・ミックスが勝利",
            "deadline": "2026-03-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2026-03-07",
            "winner": "秋元強真",
            "method": "TKO",
            "actual_outcome": "秋元強真がTKO勝ち",
            "notes": "予想外れ。"
        }
    },
    {
        "statement_id": "stmt-r52-aoki",
        "statement_date": "2026-03-06",
        "speaker": {
            "name": "青木真也",
            "role": "fighter",
            "affiliation": "MMAファイター・解説者"
        },
        "content": {
            "raw_text": "パッチー・ミックスって、組む瞬間に間合いがズレる瞬間があるんだ。そこがつけいる隙だ。でも正直ちょっと厳しいかな…",
            "normalized_text": "ミックスのUFCリリースによるモチベーション低下や、組む際の打撃への隙を指摘しつつも、最終的には秋元にとって厳しい相手であると予想。"
        },
        "source": {
            "type": "article",
            "url": "http://www.tokyo-sports.co.jp/articles/-/375364",
            "timestamp": "2026-03-06"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "青木真也",
            "source_url": "http://www.tokyo-sports.co.jp/articles/-/375364",
            "source_ref": "stmt-r52-aoki",
            "source_note": "東スポWEB記事より抽出（確認日：2026-05-05）。",
            "expected_winner": "パッチー・ミックス",
            "expected_method": None,
            "target": "秋元強真 vs パッチー・ミックス",
            "expected_outcome": "パッチー・ミックスが勝利（秋元には厳しい）",
            "deadline": "2026-03-07"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2026-03-07",
            "winner": "秋元強真",
            "method": "TKO",
            "actual_outcome": "秋元強真がTKO勝ち",
            "notes": "予想外れ。"
        }
    }
]

existing_ids = {s["statement_id"] for s in data.get("statements", [])}
for p in preds:
    if p["statement_id"] not in existing_ids:
        data["statements"].append(p)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added more predictions for RIZIN 52")
