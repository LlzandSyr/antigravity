def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    start_idx = -1
    for i, line in enumerate(lines):
        if "参" in line and "考" in line and "文" in line and "献" in line:
            start_idx = i
            break
            
    if start_idx != -1:
        print(f"Found header at line {start_idx+1}: {lines[start_idx]}")
        for j in range(start_idx, min(start_idx + 100, len(lines))):
            print(f"{j+1}: {lines[j]}")
    else:
        print("Not found")

if __name__ == "__main__":
    main()
