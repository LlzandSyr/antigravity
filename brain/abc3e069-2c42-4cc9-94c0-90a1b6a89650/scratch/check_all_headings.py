import os
import re

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("=== All Numbered Lines ===")
    for idx, l in enumerate(lines):
        line = l.strip()
        if re.match(r'^(\d+(\.\d+)*)\s+', line):
            print(f"Line {idx+1}: {line}")

if __name__ == "__main__":
    main()
