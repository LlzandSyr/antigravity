import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if os.path.exists(path_html):
        print(f"File exists! Size: {os.path.getsize(path_html)} bytes")
        # Let's search if table tags are present
        with open(path_html, "r", encoding="utf-8") as f:
            text = f.read()
        print(f"Number of table tags: {text.count('<table')}")
        print(f"Number of caption paragraphs: {text.count('class=\"caption-p\"')}")
        
        # Check if the uni-app part is in the compiled HTML
        if "pixelhub-uni-app-dev" in text:
            print("Successfully found 'pixelhub-uni-app-dev' in HTML!")
        else:
            print("Warning: 'pixelhub-uni-app-dev' NOT found in HTML")
            
        # Check if Chapter 5 contains 5.1 and 5.2 subsections
        if "5.1  系统主界面实现" in text:
            print("Successfully found '5.1  系统主界面实现' in HTML!")
        else:
            print("Warning: '5.1  系统主界面实现' NOT found in HTML")
    else:
        print("HTML file not found!")

if __name__ == "__main__":
    main()
