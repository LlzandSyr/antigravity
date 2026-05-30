import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx in range(50, 70):
        if idx < len(lines):
            print(f"{idx+1}: {lines[idx].strip()}")

if __name__ == "__main__":
    main()
