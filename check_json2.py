import json
files = ["super-rizin-2.json", "rizin-44.json", "rizin-landmark-7-azerbaijan.json"]
for fname in files:
    print(f"\n--- {fname} ---")
    try:
        with open(f"data/events/{fname}", "r", encoding="utf-8") as f:
            data = json.load(f)
        stmts = data.get("statements", [])
        if not stmts:
            print("No statements.")
        else:
            for stmt in stmts:
                print(f"{stmt.get('statement_id')}: {stmt.get('speaker', {}).get('name')} -> {stmt.get('prediction', {}).get('target')} (url: {stmt.get('source', {}).get('url')})")
    except Exception as e:
        print(f"Error reading {fname}: {e}")
