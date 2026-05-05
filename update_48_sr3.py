import json

def update_json(file_path, statements):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 既存のステートメントを取得して新しいものを追加
    existing_stmts = data.get("statements", [])
    
    # Bout filtering
    keep_bout_ids = set()
    for stmt in existing_stmts + statements:
        target = stmt["prediction"]["target"]
        if "サトシ" in target or "グスタボ" in target or "井上" in target or "スーチョル" in target:
            keep_bout_ids.update(["rizin48-10", "rizin48-11"])
        if "朝倉" in target or "平本" in target:
            keep_bout_ids.update(["super-rizin-3-bout-11"])
        if "久保" in target or "斎藤" in target:
            keep_bout_ids.update(["super-rizin-3-bout-06"])
        if "扇久保" in target or "神龍" in target:
            keep_bout_ids.update(["super-rizin-3-bout-09"])

    for card in data.get("cards", []):
        if "rizin48" in keep_bout_ids.copy().pop() or "rizin-48" in file_path:
            # 48 has target "井上直樹 vs キム・スーチョル" which is rizin48-10, "サトシ vs グスタボ" is rizin48-11
            valid_bouts = ["rizin48-10", "rizin48-11"]
        else:
            # SR3
            valid_bouts = ["super-rizin-3-bout-06", "super-rizin-3-bout-11"]

        card["bouts"] = [b for b in card.get("bouts", []) if b.get("bout_id") in valid_bouts]

    # 追加
    existing_ids = {s["statement_id"] for s in existing_stmts}
    for s in statements:
        if s["statement_id"] not in existing_ids:
            existing_stmts.append(s)

    data["statements"] = existing_stmts

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# RIZIN 48
r48_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-48.json"
r48_stmts = [
    {
        "statement_id": "stmt-rizin-48-002",
        "statement_date": "2024-09-20",
        "speaker": {
            "name": "ケイト・ロータス",
            "role": "fighter",
            "affiliation": "フリー"
        },
        "content": {
            "raw_text": "スーチョル選手の判定勝利",
            "normalized_text": "キム・スーチョルの判定勝利を予想。"
        },
        "source": {
            "type": "youtube",
            "url": "https://www.youtube.com/watch?v=rFcrXlSnrmg",
            "timestamp": "00:25:54"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ケイト・ロータス",
            "source_url": "https://www.youtube.com/watch?v=rFcrXlSnrmg",
            "source_ref": "statement_id=stmt-rizin-48-002",
            "source_note": "YouTube動画より抽出",
            "expected_winner": "キム・スーチョル",
            "expected_method": "DEC",
            "target": "井上直樹 vs キム・スーチョル",
            "expected_outcome": "キム・スーチョルが判定勝ち",
            "deadline": "2024-09-29"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-09-29",
            "winner": "井上直樹",
            "method": "KO",
            "actual_outcome": "井上直樹がKO勝ち",
            "notes": "予想は外れ。"
        }
    },
    {
        "statement_id": "stmt-rizin-48-003",
        "statement_date": "2024-09-20",
        "speaker": {
            "name": "新居すぐる",
            "role": "fighter",
            "affiliation": "HI ROLLERS ENTERTAINMENT"
        },
        "content": {
            "raw_text": "井上選手の判定勝利",
            "normalized_text": "井上直樹の判定勝利を予想。"
        },
        "source": {
            "type": "youtube",
            "url": "https://www.youtube.com/watch?v=rFcrXlSnrmg",
            "timestamp": "00:25:59"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "新居すぐる",
            "source_url": "https://www.youtube.com/watch?v=rFcrXlSnrmg",
            "source_ref": "statement_id=stmt-rizin-48-003",
            "source_note": "YouTube動画より抽出",
            "expected_winner": "井上直樹",
            "expected_method": "DEC",
            "target": "井上直樹 vs キム・スーチョル",
            "expected_outcome": "井上直樹が判定勝ち",
            "deadline": "2024-09-29"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-09-29",
            "winner": "井上直樹",
            "method": "KO",
            "actual_outcome": "井上直樹がKO勝ち",
            "notes": "勝者は的中。"
        }
    },
    {
        "statement_id": "stmt-rizin-48-004",
        "statement_date": "2024-09-20",
        "speaker": {
            "name": "新居すぐる",
            "role": "fighter",
            "affiliation": "HI ROLLERS ENTERTAINMENT"
        },
        "content": {
            "raw_text": "サトシ選手のTKO勝ち",
            "normalized_text": "ホベルト・サトシ・ソウザのTKO勝ちを予想。"
        },
        "source": {
            "type": "youtube",
            "url": "https://www.youtube.com/watch?v=rFcrXlSnrmg",
            "timestamp": "00:32:05"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "新居すぐる",
            "source_url": "https://www.youtube.com/watch?v=rFcrXlSnrmg",
            "source_ref": "statement_id=stmt-rizin-48-004",
            "source_note": "YouTube動画より抽出",
            "expected_winner": "ホベルト・サトシ・ソウザ",
            "expected_method": "TKO",
            "target": "ホベルト・サトシ・ソウザ vs ルイス・グスタボ",
            "expected_outcome": "ホベルト・サトシ・ソウザがTKO勝ち",
            "deadline": "2024-09-29"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-09-29",
            "winner": "ホベルト・サトシ・ソウザ",
            "method": "KO",
            "actual_outcome": "ホベルト・サトシ・ソウザがKO勝ち",
            "notes": "予想的中。"
        }
    }
]

update_json(r48_path, r48_stmts)

# SR3
sr3_path = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\super-rizin-3.json"
sr3_stmts = [
    {
        "statement_id": "stmt-super-rizin-3-007",
        "statement_date": "2024-07-20",
        "speaker": {
            "name": "扇久保博正",
            "role": "fighter",
            "affiliation": "パラエストラ松戸"
        },
        "content": {
            "raw_text": "斎藤選手の3ラウンドバックチョーク、1本勝ちかなと",
            "normalized_text": "斎藤裕が3Rバックチョークで一本勝ちすると予想。"
        },
        "source": {
            "type": "youtube",
            "url": "https://www.youtube.com/watch?v=WgaHYE0VrxQ",
            "timestamp": "00:06:33"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "扇久保博正",
            "source_url": "https://www.youtube.com/watch?v=WgaHYE0VrxQ",
            "source_ref": "statement_id=stmt-super-rizin-3-007",
            "source_note": "YouTube動画より抽出",
            "expected_winner": "斎藤裕",
            "expected_method": "SUB",
            "target": "久保優太 vs 斎藤裕",
            "expected_outcome": "斎藤裕が一本勝ち",
            "deadline": "2024-07-28"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-07-28",
            "winner": "久保優太",
            "method": "KO",
            "actual_outcome": "久保優太がKO勝ち",
            "notes": "予想は外れ。"
        }
    },
    {
        "statement_id": "stmt-super-rizin-3-008",
        "statement_date": "2024-07-25",
        "speaker": {
            "name": "ジョビン",
            "role": "youtuber",
            "affiliation": "フリー"
        },
        "content": {
            "raw_text": "平本蓮 判定。平本君が勝つかなっていう予想なんです全体的には",
            "normalized_text": "平本蓮の判定勝ちを予想。"
        },
        "source": {
            "type": "youtube",
            "url": "https://www.youtube.com/watch?v=j9H1Brwm9j4",
            "timestamp": "00:01:21"
        },
        "prediction": {
            "exists": True,
            "predictor_name": "ジョビン",
            "source_url": "https://www.youtube.com/watch?v=j9H1Brwm9j4",
            "source_ref": "statement_id=stmt-super-rizin-3-008",
            "source_note": "YouTube動画より抽出",
            "expected_winner": "平本蓮",
            "expected_method": "DEC",
            "target": "朝倉未来 vs 平本蓮",
            "expected_outcome": "平本蓮が判定勝ち",
            "deadline": "2024-07-28"
        },
        "verification": {
            "status": "resolved",
            "verification_date": "2024-07-28",
            "winner": "平本蓮",
            "method": "TKO",
            "actual_outcome": "平本蓮がTKO勝ち",
            "notes": "勝者は的中。"
        }
    }
]
update_json(sr3_path, sr3_stmts)

print("Updated RIZIN 48 and SR3")
