import os

def check_file(path, label):
    if not os.path.exists(path):
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"=== {label} details ===")
    
    # Let's see if we can find Chapter 5 or Chapter 4.3 sections in earlier manuscripts!
    # Specifically, check lines around Chapter 5
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "5  系统实现" in line:
            print(f"Chapter 5 found at line {i+1}")
            # Print the next 20 lines
            for j in range(i, min(i+40, len(lines))):
                print(f"  {j+1}: {lines[j]}")
            print("-" * 50)
            break

def main():
    dir_path = r"C:\Users\86135\Desktop\优秀毕业论文"
    check_file(os.path.join(dir_path, "稿件-v1.txt"), "稿件-v1.txt")
    check_file(os.path.join(dir_path, "稿件-v2.txt"), "稿件-v2.txt")
    check_file(os.path.join(dir_path, "稿件-v3.txt"), "稿件-v3.txt")

if __name__ == "__main__":
    main()
