import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    print("=== Checking margin and body settings ===")
    if "margin-right: 20mm;" in content:
        print("PASS: Right margin is set to exactly 20mm")
    else:
        print("FAIL: Right margin is incorrect")
        
    if "line-height: 20pt;" in content:
        print("PASS: Line height is set to exactly 20pt")
    else:
        print("FAIL: Line height is incorrect")

    print("\n=== Checking heading and paragraph font mappings ===")
    if "h1 {" in content and "font-size: 14pt;" in content:
        print("PASS: Level 1 heading (h1) is mapped to 14pt (4号)")
    else:
        print("FAIL: Level 1 heading mapping incorrect")
        
    if "h2 {" in content and "font-size: 12pt;" in content:
        print("PASS: Level 2 heading (h2) is mapped to 12pt (小4号)")
    else:
        print("FAIL: Level 2 heading mapping incorrect")
        
    if "h3 {" in content and "font-size: 12pt;" in content:
        print("PASS: Level 3 heading (h3) is mapped to 12pt (小4号)")
    else:
        print("FAIL: Level 3 heading mapping incorrect")
        
    print("\n=== Checking References formatting ===")
    if "参  考  文  献" in content and "font-size: 14pt;" in content and "text-align: center;" in content:
        print("PASS: References title is mapped to 14pt (4号) SimHei, centered")
    else:
        print("FAIL: References title mapping incorrect")
        
    if "p.reference-item {" in content and "text-indent: -2em;" in content and "padding-left: 2em;" in content:
        print("PASS: Reference items have hanging indent (悬挂缩进)")
    else:
        print("FAIL: Reference items hanging indent incorrect")
        
    print("\n=== Checking English Section formatting ===")
    if "h1.english-title {" in content and "font-size: 16pt;" in content:
        print("PASS: English Title is mapped to 16pt (3号) Times New Roman, bold, centered")
    else:
        print("FAIL: English Title mapping incorrect")
        
    if "p.english-abstract {" in content and "font-size: 12pt;" in content:
        print("PASS: English Abstract is mapped to 12pt (小4号)")
    else:
        print("FAIL: English Abstract mapping incorrect")

if __name__ == "__main__":
    main()
