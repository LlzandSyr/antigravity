def main():
    path_v4 = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_v4, "r", encoding="utf-8") as f:
        content = f.read()
        
    idx = content.find("参  考  文  献")
    if idx != -1:
        print("=== Verification of v4 Draft References ===")
        print(content[idx:idx+1200])
    else:
        print("References not found")

if __name__ == "__main__":
    main()
