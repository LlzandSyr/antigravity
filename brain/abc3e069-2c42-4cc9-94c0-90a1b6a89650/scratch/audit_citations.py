import os
import re

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We ignore the bibliography section at the end
    bib_idx = content.find("参  考  文  献")
    if bib_idx != -1:
        text_before_bib = content[:bib_idx]
    else:
        text_before_bib = content
        
    # Find all citations like [1], [2], [3], etc.
    matches = list(re.finditer(r"\[\d+\]", text_before_bib))
    
    seen = {}
    dupes = []
    print(f"=== Total citation matches: {len(matches)} ===")
    for m in matches:
        tag = m.group(0)
        start = m.start()
        # Get context
        context = text_before_bib[max(0, start-40):min(len(text_before_bib), start+40)].replace("\n", " ")
        if tag in seen:
            print(f"DUPLICATE citation: {tag} at index {start}")
            print(f"  Context: ... {context} ...")
            dupes.append((tag, start))
        else:
            seen[tag] = start
            print(f"FIRST occurrence of: {tag} at index {start}")
            print(f"  Context: ... {context} ...")
            
if __name__ == "__main__":
    main()
