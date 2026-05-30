import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.txt"
    with open(path_txt, "r", encoding="gb18030") as f:
        content = f.read()
    # Find Section 6.3 in GB18030
    idx = content.find("6.3")
    if idx != -1:
        # Let's search for "6.3.1" or "测试用例" after the index
        print(content[idx:idx+1500])

if __name__ == "__main__":
    main()
