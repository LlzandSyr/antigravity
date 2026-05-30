import os
import glob

def main():
    folder = r"C:\Users\86135\Desktop\优秀毕业论文"
    # Find all files recursively
    files = glob.glob(os.path.join(folder, "**", "*"), recursive=True)
    for path in files:
        if os.path.isdir(path):
            continue
        # Read file with multiple encodings
        for enc in ["utf-8", "gbk", "gb18030"]:
            try:
                with open(path, "r", encoding=enc) as f:
                    content = f.read()
                if "致谢" in content or "致  谢" in content:
                    print(f"FOUND '致谢' in {path} (encoding {enc})")
                    break
            except Exception:
                pass

if __name__ == "__main__":
    main()
