def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    # Find line containing "参考文献" or similar and print subsequent lines
    start_idx = -1
    for i, line in enumerate(lines):
        if "参  考  文  献" in line or line.strip() == "参考文献":
            start_idx = i
            break
            
    if start_idx != -1:
        print(f"=== Original Bibliography starting at line {start_idx+1} ===")
        for j in range(start_idx, min(start_idx + 80, len(lines))):
            print(f"{j+1}: {lines[j]}")
    else:
        print("Could not find Bibliography header")

if __name__ == "__main__":
    main()
