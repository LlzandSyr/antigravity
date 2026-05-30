import os
import time

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if os.path.exists(path_html):
        mtime = os.path.getmtime(path_html)
        print("Modified time:", time.ctime(mtime))
        print("Size:", os.path.getsize(path_html))
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()
