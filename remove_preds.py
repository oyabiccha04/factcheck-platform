import json

filepath = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-52.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

to_remove = ["stmt-r52-2ch", "stmt-r52-tapology"]
data["statements"] = [s for s in data.get("statements", []) if s.get("statement_id") not in to_remove]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Removed 2ch and tapology predictions")
