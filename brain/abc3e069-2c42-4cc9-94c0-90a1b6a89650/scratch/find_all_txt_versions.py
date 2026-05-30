import os

def check_tech_section(path, label):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find "2  相关技术介绍" and print next 500 characters
    idx = content.find("2  相关技术介绍")
    if idx != -1:
        print(f"=== {label} ===")
        print(content[idx:idx+1500])
    else:
        print(f"=== {label} (Not found '2  相关技术介绍') ===")

def main():
    dir_path = r"C:\Users\86135\Desktop\优秀毕业论文"
    for f in sorted(os.listdir(dir_path)):
        if f.endswith(".txt") and "稿件" in f:
            check_tech_section(os.path.join(dir_path, f), f)

if __name__ == "__main__":
    main()
