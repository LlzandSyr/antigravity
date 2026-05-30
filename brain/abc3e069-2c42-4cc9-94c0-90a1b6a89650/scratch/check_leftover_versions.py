import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    versions = ["Vue 3", "2.7.6", "5.7", "17", "3.9", "22", "10.9", "5.5"]
    print("=== Leftover Version Checks ===")
    for v in versions:
        count = content.count(v)
        print(f"Version: {v} - Count: {count}")
        if count > 0:
            lines = content.splitlines()
            for idx, l in enumerate(lines):
                if v in l:
                    print(f"  Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
