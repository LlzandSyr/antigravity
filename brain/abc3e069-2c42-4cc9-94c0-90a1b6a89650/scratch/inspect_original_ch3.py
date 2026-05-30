import os

def main():
    path_orig = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_orig):
        print("File not found")
        return
        
    with open(path_orig, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    print("=== Searching for 经济可行性 in 大论文原文.md ===")
    for idx, l in enumerate(lines):
        if "经济可行性" in l or "计费" in l or "百炼" in l:
            print(f"Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
