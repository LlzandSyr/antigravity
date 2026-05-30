def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if "表1" in line or "表2" in line or "表3" in line or "表4" in line or "表5" in line or "表6" in line or "表7" in line or "表8" in line or "表9" in line:
            print(f"Line {i+1}: {line.strip()[:100]}")

if __name__ == "__main__":
    main()
