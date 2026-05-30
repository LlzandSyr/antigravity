import os

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
    # Let's search for "6.3  " or "6.3.1" or "测试用例"
    idx = content.find("6.3")
    if idx != -1:
        print(content[idx:idx+1500])
    else:
        print("6.3 not found in markdown file")

if __name__ == "__main__":
    main()
