import os

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_md):
        print("大论文原文.md not found")
        return
        
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Search for "谢" or "致谢"
    if "谢" in content:
        print("Found '谢' in 大论文原文.md!")
        # Let's find all occurrences of "谢" and print context
        for idx in range(len(content)):
            if content[idx] == "谢":
                print(content[max(0, idx-50):idx+50])
                print("-" * 30)

if __name__ == "__main__":
    main()
