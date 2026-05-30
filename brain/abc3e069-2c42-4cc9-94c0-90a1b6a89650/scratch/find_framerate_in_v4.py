import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    path_orig = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    
    if os.path.exists(path_txt):
        with open(path_txt, "r", encoding="utf-8") as f:
            txt_content = f.read()
        print("=== occurrences of '帧率' in 稿件-v4.txt ===")
        lines = txt_content.splitlines()
        for idx, l in enumerate(lines):
            if "帧率" in l:
                print(f"Line {idx+1}: {l.strip()}")
                
    if os.path.exists(path_orig):
        with open(path_orig, "r", encoding="utf-8") as f:
            orig_content = f.read()
        print("=== occurrences of '帧率' in 大论文原文.md ===")
        lines = orig_content.splitlines()
        for idx, l in enumerate(lines):
            if "帧率" in l:
                print(f"Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
