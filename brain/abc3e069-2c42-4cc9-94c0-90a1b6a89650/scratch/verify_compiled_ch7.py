import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    print("=== Compiled HTML uni-app sentence ===")
    lines = content.splitlines()
    for idx, l in enumerate(lines):
        if "uni-app" in l:
            print(f"Line {idx+1}: {l.strip()}")
            
if __name__ == "__main__":
    main()
