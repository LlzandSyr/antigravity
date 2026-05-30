import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("=== Figure 1 in HTML ===")
    for idx, l in enumerate(lines):
        if "图1" in l or "图 1" in l:
            for j in range(max(0, idx-2), min(len(lines), idx+6)):
                print(f"{j+1}: {lines[j].strip()}")
            print("-" * 50)
            
    print("=== Table 1 in HTML ===")
    for idx, l in enumerate(lines):
        if "表1" in l or "表 1" in l:
            for j in range(max(0, idx-2), min(len(lines), idx+6)):
                print(f"{j+1}: {lines[j].strip()}")
            print("-" * 50)

if __name__ == "__main__":
    main()
