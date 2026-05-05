import glob

for file in ["QUX7tGg0PyA.(ext)s.txt", "wjQJDW3jQJY.(ext)s.txt", "tf0-buC1RPk.(ext)s.txt", "twizgK-OMFo.(ext)s.txt"]:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"--- {file} ---")
        print(content[:300])
        print("...")
