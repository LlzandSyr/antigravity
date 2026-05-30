import re

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    print("=== Original Citations in 大论文原文.md ===")
    for i, line in enumerate(lines):
        matches = re.findall(r'(\[[1-9]\d*\])', line)
        if matches:
            # Print line number, the matches, and the clean text of the line
            print(f"Line {i+1} ({matches}): {line.strip()[:100]}")

if __name__ == "__main__":
    main()
