import os
import glob

def main():
    folder = r"C:\Users\86135\Desktop\优秀毕业论文"
    files = glob.glob(os.path.join(folder, "**", "*"), recursive=True)
    
    print("=== Searching for '致谢' in manuscript folder ===")
    for path in files:
        if os.path.isdir(path):
            continue
        if any(ext in path.lower() for ext in [".txt", ".html", ".md"]):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "致谢" in content or "致  谢" in content:
                    print(f"Found in: {os.path.basename(path)}")
            except Exception:
                try:
                    with open(path, "r", encoding="gbk") as f:
                        content = f.read()
                    if "致谢" in content or "致  谢" in content:
                        print(f"Found in: {os.path.basename(path)} (GBK)")
                except Exception:
                    pass

if __name__ == "__main__":
    main()
