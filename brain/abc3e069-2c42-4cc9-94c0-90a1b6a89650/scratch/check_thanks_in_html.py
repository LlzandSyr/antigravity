import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "谢" in content:
        print("Found '谢' in HTML!")
        # Print surrounding text
        for idx in range(len(content)):
            if content[idx] == "谢":
                print(content[max(0, idx-50):idx+50])
                print("-" * 30)
    else:
        print("'谢' NOT found in HTML")

if __name__ == "__main__":
    main()
