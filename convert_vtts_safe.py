import os
import re
import glob

vtt_files = glob.glob("*.vtt")
for f in vtt_files:
    try:
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
        
        # simple vtt parse
        lines = content.split('\n')
        text_lines = []
        for line in lines:
            if not re.match(r'^\d{2}:\d{2}', line) and 'WEBVTT' not in line and 'Kind: captions' not in line and 'Language:' not in line and line.strip() != '':
                clean_line = re.sub(r'<[^>]+>', '', line)
                if clean_line.strip() and clean_line.strip() not in text_lines[-1:]:
                    text_lines.append(clean_line.strip())
                    
        out_name = f.split("]")[0].split("[")[-1] + f.split("]")[-1]
        out_name = out_name.replace(".vtt", ".txt")
        with open(out_name, "w", encoding="utf-8") as out_file:
            out_file.write(" ".join(text_lines))
    except Exception as e:
        pass
