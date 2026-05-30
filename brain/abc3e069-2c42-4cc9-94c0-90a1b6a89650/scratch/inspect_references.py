import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    print("=== Table and Figure lines in 稿件-v4.txt ===")
    for idx, l in enumerate(lines):
        if "表" in l or "图" in l:
            # If the line itself is a caption (e.g., "图1" or "表1" alone)
            is_caption = l.strip().startswith("图") or l.strip().startswith("表")
            print(f"Line {idx+1} ({'Caption' if is_caption else 'Text'}): {l.strip()}")

if __name__ == "__main__":
    main()
