import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx, l in enumerate(lines):
        if "5.2" in l:
            print(f"Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
