import re

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if re.search(r'图\d', line) or re.search(r'表\d', line):
            print(f"Line {i+1}: {line.strip()}")

if __name__ == "__main__":
    main()
