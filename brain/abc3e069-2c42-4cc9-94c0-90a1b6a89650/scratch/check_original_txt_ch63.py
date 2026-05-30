import os

def main():
    path_main = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.txt"
    if not os.path.exists(path_main):
        print("Main thesis file not found")
        return
        
    with open(path_main, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find 6.3
    idx = content.find("6.3")
    if idx != -1:
        print(content[idx:idx+1500])

if __name__ == "__main__":
    main()
