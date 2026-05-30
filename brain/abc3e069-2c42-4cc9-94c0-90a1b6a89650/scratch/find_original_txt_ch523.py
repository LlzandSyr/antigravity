import os

def main():
    path_orig = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_orig):
        print("File not found")
        return
        
    with open(path_orig, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    for idx, l in enumerate(lines):
        if "图生视频" in l:
            print(f"Line {idx+1}: {l.strip()}")
            # Print adjacent lines
            for j in range(max(0, idx-2), min(len(lines), idx+5)):
                print(f"  {j+1}: {lines[j]}")
            print("-" * 50)

if __name__ == "__main__":
    main()
