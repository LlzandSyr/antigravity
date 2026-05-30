import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx, l in enumerate(lines):
        if "表1" in l:
            print(f"=== Found '表1' on Line {idx+1} ===")
            for j in range(max(0, idx-5), min(len(lines), idx+15)):
                print(f"{j+1}: {lines[j].strip()}")
            print("-" * 50)

if __name__ == "__main__":
    main()
