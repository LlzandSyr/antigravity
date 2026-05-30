import os

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_md):
        print("File not found")
        return
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    idx = content.find("图5.22")
    if idx != -1:
        print("=== Text around 图5.22 ===")
        print(content[idx-600:idx+600])

if __name__ == "__main__":
    main()
