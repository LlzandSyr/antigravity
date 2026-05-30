import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"File Size: {os.path.getsize(path_html)} bytes")
    
    # Check tables count
    tables_count = content.count("<table")
    print(f"Number of table elements: {tables_count}")
    
    # Check figure placeholders count
    placeholders = content.count("截图占位")
    print(f"Dashed box placeholders count: {placeholders}")
    
    # Check centered captions count
    captions = content.count('text-align: center; margin:')
    print(f"Centered captions count: {captions}")
    
    # Print the captions text
    lines = content.splitlines()
    for l in lines:
        if "text-align: center; margin:" in l:
            print("Caption Line:", l.strip())

if __name__ == "__main__":
    main()
