import os

def main():
    paths = [
        r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt",
        r"C:\Users\86135\Desktop\优秀毕业论文\bak\稿件-v4.txt",
        r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    ]
    for path in paths:
        if not os.path.exists(path):
            print(f"Not found: {path}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "致谢" in content or "致  谢" in content:
            print(f"Found in: {path}!")
            # Find index
            idx = content.find("致谢")
            if idx == -1:
                idx = content.find("致  谢")
            print(content[max(0, idx-100):idx+300])
            print("="*60)
        else:
            print(f"Not found in: {path}")

if __name__ == "__main__":
    main()
