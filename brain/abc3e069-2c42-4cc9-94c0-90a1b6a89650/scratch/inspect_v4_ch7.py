import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    path_orig = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    
    if os.path.exists(path_txt):
        with open(path_txt, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print("=== uni-app in 稿件-v4.txt ===")
        for idx, l in enumerate(lines):
            if "uni-app" in l or "跨端" in l:
                print(f"Line {idx+1}: {l.strip()}")
                
    if os.path.exists(path_orig):
        with open(path_orig, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print("=== uni-app in 大论文原文.md ===")
        for idx, l in enumerate(lines):
            if "uni-app" in l or "跨端" in l:
                print(f"Line {idx+1}: {l.strip()}")

if __name__ == "__main__":
    main()
