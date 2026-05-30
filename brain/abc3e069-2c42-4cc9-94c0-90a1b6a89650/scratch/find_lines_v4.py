def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if "引言" in line or "课题背景" in line or "国内外" in line:
            print(f"Line {i+1}: {line.strip()}")

if __name__ == "__main__":
    main()
