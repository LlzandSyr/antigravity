import os
import re

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_md):
        print("File not found")
        return
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    idx = content.find("5  系统实现")
    if idx != -1:
        ch5_text = content[idx:]
        # Find lines containing "图" or "图5" or "图4" or "图3"
        lines = ch5_text.split("\n")
        print("=== Lines with figure captions in Chapter 5 ===")
        for line in lines:
            if "**图" in line or "<center>**图" in line or "<center>**表" in line or "**表" in line:
                if "5." in line or "图" in line:
                    print(line)

if __name__ == "__main__":
    main()
