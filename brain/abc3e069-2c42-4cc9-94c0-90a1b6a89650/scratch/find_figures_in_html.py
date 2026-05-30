import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx, l in enumerate(lines):
        if "截图占位符" in l or "图" in l:
            if "截图占位符" in l or ("图" in l and len(l) < 200 and ("图1" in l or "图2" in l or "图3" in l or "图4" in l or "图5" in l or "图6" in l or "图7" in l)):
                print(f"Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
