import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    print("=== Last 25 lines of the HTML ===")
    for l in lines[-25:]:
        print(l.strip())

if __name__ == "__main__":
    main()
