def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    
    # Try reading as GBK
    try:
        with open(path_md, "r", encoding="gbk") as f:
            content = f.read()
        print("Successfully read as GBK!")
    except Exception as e:
        print(f"Failed to read as GBK: {e}")
        # Try GB18030
        try:
            with open(path_md, "r", encoding="gb18030") as f:
                content = f.read()
            print("Successfully read as GB18030!")
        except Exception as e2:
            print(f"Failed to read as GB18030: {e2}")
            return
            
    lines = content.split('\n')
    start_idx = -1
    for i in range(len(lines) - 1, -1, -1):
        if "参" in lines[i] and "考" in lines[i] and "文" in lines[i] and "献" in lines[i]:
            start_idx = i
            break
            
    if start_idx != -1:
        print(f"Found bibliography header at line {start_idx+1}: {lines[start_idx]}")
        for j in range(start_idx, min(start_idx + 30, len(lines))):
            print(f"{j+1}: {lines[j]}")

if __name__ == "__main__":
    main()
