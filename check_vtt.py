import re

def print_around(filename, target_s, window=120):
    print(f"\n--- {filename} around {target_s}s ---")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        blocks = content.split("\n\n")
        for block in blocks:
            m = re.search(r"(\d{2}):(\d{2}):(\d{2})\.\d{3}", block)
            if m:
                h, m_min, s = map(int, m.groups())
                t_s = h * 3600 + m_min * 60 + s
                if target_s - window <= t_s <= target_s + window:
                    text = "\n".join(block.split("\n")[2:])
                    text = re.sub(r"<[^>]+>", "", text)
                    # print on one line to avoid too much output
                    print(f"[{h:02}:{m_min:02}:{s:02}] {text.replace(chr(10), ' ').strip()}")
    except Exception as e:
        print(e)

print_around("ougikubo_39.ja.vtt", 945)
print_around("satoshi_39.ja.vtt", 615)
