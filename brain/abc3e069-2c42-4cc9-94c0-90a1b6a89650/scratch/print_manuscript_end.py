import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    idx = content.find("参  考  文  献")
    if idx != -1:
        print("=== End of 稿件-v4.txt ===")
        print(content[idx:])
    else:
        print("参考文献 not found")

if __name__ == "__main__":
    main()
