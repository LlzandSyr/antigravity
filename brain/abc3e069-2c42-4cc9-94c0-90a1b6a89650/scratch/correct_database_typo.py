import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if os.path.exists(path_txt):
        with open(path_txt, "r", encoding="utf-8") as f:
            content = f.read()
        if "图生图" in content:
            content = content.replace("图生图", "文生视频、图生视频")
            with open(path_txt, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully corrected typo in 稿件-v4.txt!")
            
if __name__ == "__main__":
    main()
