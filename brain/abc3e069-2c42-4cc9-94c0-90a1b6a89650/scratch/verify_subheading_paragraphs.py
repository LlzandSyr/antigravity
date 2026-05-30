import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("=== Subheadings 5.2.x in HTML ===")
    for idx, l in enumerate(lines):
        if "5.2." in l:
            print(f"Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
