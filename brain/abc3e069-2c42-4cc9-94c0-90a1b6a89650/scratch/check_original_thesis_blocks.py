import os

def main():
    path_main = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_main):
        print("Main thesis file not found")
        return
        
    with open(path_main, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Search for "6.3" or "4.3" or "数据库设计" or "测试用例"
    keywords = ["6.3  测试用例", "4.3.2  逻辑结构设计", "5  系统实现"]
    for kw in keywords:
        idx = content.find(kw)
        if idx != -1:
            print(f"=== Found '{kw}' ===")
            print(content[idx:idx+1200])
            print("="*60)
        else:
            print(f"Keyword '{kw}' not found")

if __name__ == "__main__":
    main()
