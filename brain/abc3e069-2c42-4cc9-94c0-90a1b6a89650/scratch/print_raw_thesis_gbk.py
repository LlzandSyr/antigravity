import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    for enc in ["utf-8", "gb18030", "gbk"]:
        try:
            with open(path_txt, "r", encoding=enc) as f:
                content = f.read()
            print(f"=== Encoding {enc} ===")
            # Let's search for "6.3" or "测试用例"
            idx = content.find("6.3")
            if idx != -1:
                print(content[idx:idx+1000])
                print("="*60)
                break
        except Exception as e:
            print(f"Failed with {enc}: {e}")

if __name__ == "__main__":
    main()
