import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    idx = content.find("致谢")
    if idx != -1:
        print(f"Found '致谢' at character {idx}!")
        print(content[idx-100:idx+300])
    else:
        print("No '致谢' found in 稿件-v4.txt")

if __name__ == "__main__":
    main()
