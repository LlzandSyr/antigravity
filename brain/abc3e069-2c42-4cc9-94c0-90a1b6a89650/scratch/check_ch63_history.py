import os

def check_ch63(path, label):
    if not os.path.exists(path):
        print(f"{label} not found")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    idx = content.find("6.3  测试用例")
    if idx != -1:
        print(f"=== {label} Chapter 6.3 ===")
        print(content[idx:idx+800])
        print("="*60)
    else:
        print(f"6.3 not found in {label}")

def main():
    dir_path = r"C:\Users\86135\Desktop\优秀毕业论文"
    check_ch63(os.path.join(dir_path, "稿件-v1.txt"), "稿件-v1.txt")
    check_ch63(os.path.join(dir_path, "稿件-v2.txt"), "稿件-v2.txt")
    check_ch63(os.path.join(dir_path, "稿件-v3.txt"), "稿件-v3.txt")

if __name__ == "__main__":
    main()
