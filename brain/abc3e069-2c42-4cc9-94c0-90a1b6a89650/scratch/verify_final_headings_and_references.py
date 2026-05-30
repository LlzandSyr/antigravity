import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("=== Compiled HTML Heading Checks ===")
    for idx, l in enumerate(lines):
        if "6.2" in l or "6.3" in l:
            print(f"Line {idx+1}: {l.strip()}")
            
    print("\n=== Compiled HTML Figure & Table Reference Checks ===")
    for idx, l in enumerate(lines):
        if "如图" in l or "如表" in l:
            print(f"Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
