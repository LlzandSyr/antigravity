import os
import glob

def main():
    folder = r"C:\Users\86135\Desktop\优秀毕业论文"
    files = glob.glob(os.path.join(folder, "**", "*"), recursive=True)
    
    print("=== Searching for 'Adobe' in all files ===")
    for path in files:
        if os.path.isdir(path):
            continue
        for enc in ["utf-8", "gbk", "gb18030"]:
            try:
                with open(path, "r", encoding=enc) as f:
                    content = f.read()
                if "Adobe" in content or "adobe" in content.lower():
                    print(f"FOUND 'Adobe' in {path} (encoding {enc})")
                    # print context
                    idx = content.lower().find("adobe")
                    print(content[max(0, idx-100):idx+300])
                    print("=" * 50)
                    break
            except Exception:
                pass

if __name__ == "__main__":
    main()
