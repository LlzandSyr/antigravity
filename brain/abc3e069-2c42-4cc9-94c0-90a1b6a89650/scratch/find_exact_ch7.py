def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    start_idx = content.find("7  总结与展望")
    end_idx = content.find("参  考  文  献")
    
    if start_idx != -1 and end_idx != -1:
        print("=== Chapter 7 in File ===")
        print(repr(content[start_idx:end_idx]))
    else:
        print(f"Error: start={start_idx}, end={end_idx}")

if __name__ == "__main__":
    main()
