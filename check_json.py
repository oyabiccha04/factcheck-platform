import json

files = ["rizin-40.json", "rizin-41.json", "rizin-42.json", "rizin-43.json"]

for fname in files:
    print(f"\n--- {fname} ---")
    path = f"data/events/{fname}"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    stmts = data.get("statements", [])
    if not stmts:
        print("No statements.")
    for stmt in stmts:
        print(f"{stmt['statement_id']}: {stmt['speaker']['name']} -> {stmt['prediction'].get('target')} ({stmt['source'].get('url')})")
