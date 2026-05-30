import os

def main():
    path_md = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    with open(path_md, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's search for "6.3.1" or "## 6.3" further down in the file
    # We can find all indexes of "6.3.1" and print the content from the second index
    idx = -1
    for _ in range(2):
        idx = content.find("6.3.1", idx + 1)
        if idx == -1:
            break
            
    if idx != -1:
        print("=== Section 6.3.1 ===")
        print(content[idx:idx+1500])
    else:
        print("Could not find section 6.3.1 details")

if __name__ == "__main__":
    main()
