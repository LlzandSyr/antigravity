def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    print(f"Total lines: {len(lines)}")
    
    # Let's search for "参  考  文  献" or "参考文献"
    found_idx = -1
    for i in range(len(lines) - 1, -1, -1):
        if "参" in lines[i] and "考" in lines[i] and "文" in lines[i] and "献" in lines[i]:
            found_idx = i
            break
            
    if found_idx != -1:
        print(f"Found bibliography header at line {found_idx+1}: {lines[found_idx]}")
        for j in range(found_idx, min(found_idx + 80, len(lines))):
            print(f"{j+1}: {lines[j]}")
    else:
        # Just print the last 80 lines of the file
        print("Not found, printing last 80 lines:")
        for j in range(max(0, len(lines) - 80), len(lines)):
            print(f"{j+1}: {lines[j]}")

if __name__ == "__main__":
    main()
