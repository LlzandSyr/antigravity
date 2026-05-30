import os

def check_file(file_path):
    if not os.path.exists(file_path):
        print(f"Not found: {file_path}")
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    count = content.count("帧率")
    print(f"File: {os.path.basename(file_path)} - '帧率' count: {count}")
    if count > 0:
        lines = content.splitlines()
        for idx, l in enumerate(lines):
            if "帧率" in l:
                print(f"  Line {idx+1}: {l.strip()}")

def main():
    check_file(r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md")
    check_file(r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt")
    check_file(r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html")

if __name__ == "__main__":
    main()
