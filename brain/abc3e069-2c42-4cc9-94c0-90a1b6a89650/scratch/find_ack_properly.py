import os

def main():
    # Use dynamic path matching or walk
    desktop = r"C:\Users\86135\Desktop"
    found_dir = None
    for name in os.listdir(desktop):
        if "优秀毕业论文" in name or name.startswith("优秀"):
            found_dir = os.path.join(desktop, name)
            break
            
    if not found_dir:
        print("Folder not found")
        return
        
    print(f"Searching in folder: {found_dir}")
    for root, dirs, files in os.walk(found_dir):
        for file in files:
            if "稿件-v4" in file or "稿件.html" in file:
                path = os.path.join(root, file)
                print(f"Reading file: {path}")
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "致谢" in content or "致  谢" in content:
                    print(f"Found '致谢' in {file}!")
                    # Find index
                    idx = content.find("致谢")
                    if idx == -1:
                        idx = content.find("致  谢")
                    print(content[max(0, idx-100):idx+300])
                    print("="*60)
                else:
                    print(f"'致谢' NOT found in {file}")

if __name__ == "__main__":
    main()
