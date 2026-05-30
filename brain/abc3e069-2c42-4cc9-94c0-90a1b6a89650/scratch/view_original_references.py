import re

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    start_idx = -1
    for i, line in enumerate(lines):
        if "参  考  文  献" in line or line.strip() == "参考文献":
            start_idx = i
            break
            
    if start_idx != -1:
        print("=== Bibliography Items ===")
        ref_count = 0
        for j in range(start_idx, len(lines)):
            line = lines[j].strip()
            if re.match(r'^\[\d+\]', line):
                print(f"Ref Line: {line}")
                ref_count += 1
                if ref_count >= 15:
                    break
    else:
        print("Bibliography not found")

if __name__ == "__main__":
    main()
