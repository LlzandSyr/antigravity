def main():
    path_v4 = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_v4, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("=== Verification of v4 draft Chapter 1 ===")
    for i in range(9, 25):
        if i < len(lines):
            print(f"Line {i+1}: {lines[i].strip()}")

if __name__ == "__main__":
    main()
