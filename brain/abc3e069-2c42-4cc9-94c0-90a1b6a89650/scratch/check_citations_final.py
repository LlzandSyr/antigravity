import os
import re

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all citations like [1], [2], [3-5], etc.
    citations = re.findall(r"\[\d+\]|\[\d+-\d+\]", content)
    print(f"Total citation tags found in text: {len(citations)}")
    print(f"Unique citations found: {sorted(list(set(citations)))}")
    
    # Check bibliography
    bib_idx = content.find("参  考  文  献")
    if bib_idx != -1:
        bib_part = content[bib_idx:]
        bib_items = re.findall(r"^\[\d+\].*", bib_part, re.MULTILINE)
        print(f"Total bibliography items found: {len(bib_items)}")
        for item in bib_items:
            print(item)
            
if __name__ == "__main__":
    main()
