import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Print the lines around "表1" in the text file
    lines = content.splitlines()
    for idx, l in enumerate(lines):
        if "表1" in l or "表 1" in l or "图1" in l or "图 1" in l:
            print(f"=== Line {idx+1} ===")
            for j in range(max(0, idx-3), min(len(lines), idx+4)):
                print(f"{j+1}: {lines[j]}")
            print("-" * 50)

if __name__ == "__main__":
    main()
