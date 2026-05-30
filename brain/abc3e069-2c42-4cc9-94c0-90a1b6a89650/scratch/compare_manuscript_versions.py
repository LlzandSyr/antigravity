import os

def check_file(path, label):
    if not os.path.exists(path):
        print(f"{label} does not exist")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    print(f"=== {label} ===")
    for i, line in enumerate(lines):
        if "表1" in line or "表5" in line or "表2" in line:
            print(f"Line {i+1}: {line.strip()[:100]}")

def main():
    dir_path = r"C:\Users\86135\Desktop\优秀毕业论文"
    check_file(os.path.join(dir_path, "稿件-v1.txt"), "稿件-v1.txt")
    check_file(os.path.join(dir_path, "稿件-v2.txt"), "稿件-v2.txt")
    check_file(os.path.join(dir_path, "稿件-v3.txt"), "稿件-v3.txt")
    check_file(os.path.join(dir_path, "稿件-v4.txt"), "稿件-v4.txt")

if __name__ == "__main__":
    main()
