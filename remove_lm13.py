import json

filepath = r"c:\Users\oyabi\OneDrive\デスクトップ\20260317_forecastcheck\factcheck-platform-main\data\events\rizin-landmark-13-fukuoka.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

to_remove = ["stmt-lm13-hiramoto"]
data["statements"] = [s for s in data.get("statements", []) if s.get("statement_id") not in to_remove]

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Removed 2ch summary prediction from LM13")
