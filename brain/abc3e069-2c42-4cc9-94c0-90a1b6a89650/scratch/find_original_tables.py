def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    print("=== Original Tables in 大论文原文.md ===")
    for i, line in enumerate(lines):
        if "user" in line.lower() or "表" in line or "字段" in line:
            print(f"Line {i+1}: {line.strip()[:100]}")

if __name__ == "__main__":
    main()
