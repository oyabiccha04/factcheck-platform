import re

def vtt_to_txt(vtt_file, txt_file):
    try:
        with open(vtt_file, "r", encoding="utf-8") as f:
            content = f.read()
        blocks = content.split("\n\n")
        with open(txt_file, "w", encoding="utf-8") as out:
            for block in blocks:
                m = re.search(r"(\d{2}):(\d{2}):(\d{2})\.\d{3}", block)
                if m:
                    h, m_min, s = map(int, m.groups())
                    text = "\n".join(block.split("\n")[2:])
                    text = re.sub(r"<[^>]+>", "", text).replace("\n", " ").strip()
                    if text:
                        out.write(f"[{h:02}:{m_min:02}:{s:02}] {text}\n")
    except Exception as e:
        print(e)

vtt_to_txt("jobin_39.ja.vtt", "jobin_39.txt")
vtt_to_txt("kurumi_39.ja.vtt", "kurumi_39.txt")
vtt_to_txt("rizin40_unext.ja.vtt", "rizin40_unext.txt")
