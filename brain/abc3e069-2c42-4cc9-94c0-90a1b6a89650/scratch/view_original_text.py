def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    print("=== Original text of Chapter 1.1 ===")
    for j in range(440, 485):
        if j < len(lines):
            print(f"Line {j+1}: {lines[j]}")

if __name__ == "__main__":
    main()
