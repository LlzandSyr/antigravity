import re

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v3.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    for i, line in enumerate(lines):
        matches = re.findall(r'(\[\d+\])', line)
        if matches:
            print(f"Line {i+1} ({matches}): {line.strip()[:100]}")

if __name__ == "__main__":
    main()
