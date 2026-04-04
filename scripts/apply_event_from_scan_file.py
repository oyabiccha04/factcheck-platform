#!/usr/bin/env python3
"""スキャン結果 JSON を興行イベント JSON に反映する（API は呼ばない）。"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import boxing_youtube_prediction_scan as scan  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="scan JSON を event JSON に適用")
    p.add_argument("scan_json", type=Path, help="boxing_youtube_prediction_scan の出力 JSON")
    p.add_argument("event_json", type=Path, help="更新する興行 JSON")
    p.add_argument("--confirm-date", default="2026-04-04")
    args = p.parse_args()

    scan_path = args.scan_json if args.scan_json.is_absolute() else REPO_ROOT / args.scan_json
    event_path = args.event_json if args.event_json.is_absolute() else REPO_ROOT / args.event_json
    report = json.loads(scan_path.read_text(encoding="utf-8"))
    n, log = scan.apply_report_to_event_json(event_path, report, confirm_date=args.confirm_date)
    print(f"更新 {n} 件: {event_path}")
    for line in log:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
