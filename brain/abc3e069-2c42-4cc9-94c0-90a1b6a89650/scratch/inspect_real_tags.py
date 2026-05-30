import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    print("=== A standard paragraph line ===")
    for l in lines:
        if "课题背景" in l and "<p" in l:
            print(l.strip())
            break
            
    print("\n=== A reference item line ===")
    for l in lines:
        if "[1]" in l:
            print(l.strip())
            break
            
    print("\n=== English abstract line ===")
    for l in lines:
        if "Abstract:" in l:
            print(l.strip())
            break

if __name__ == "__main__":
    main()
