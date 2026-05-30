def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    # Let's print tables around user table (around line 978 in original)
    print("=== Table 4.1 in 大论文原文.md ===")
    for j in range(970, 995):
        if j < len(lines):
            print(f"{j+1}: {lines[j]}")
            
    print("\n=== Table 4.2 in 大论文原文.md ===")
    for j in range(995, 1025):
        if j < len(lines):
            print(f"{j+1}: {lines[j]}")

if __name__ == "__main__":
    main()
