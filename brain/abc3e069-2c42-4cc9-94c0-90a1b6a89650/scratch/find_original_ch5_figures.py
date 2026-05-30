import os
import re

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_md):
        print("File not found")
        return
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    idx = content.find("5  系统实现")
    if idx != -1:
        ch5_text = content[idx:idx+15000]
        # Find all Figure headings (图5.x or 图x)
        figs = re.findall(r"图[0-9\.]+\s+\w+", ch5_text)
        print("=== Figures found in Chapter 5 of original ===")
        for fig in figs:
            print(fig)
            
        # Also print Section headings in Chapter 5
        print("\n=== Subsections found ===")
        headings = re.findall(r"#{2,4}\s+[0-9\.]+\s+\w+", ch5_text)
        for h in headings:
            print(h)

if __name__ == "__main__":
    main()
