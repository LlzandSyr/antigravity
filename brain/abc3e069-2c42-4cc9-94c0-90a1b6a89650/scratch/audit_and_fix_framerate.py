import os

def fix_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replacements to remove '帧率' and replace with '分辨率' or other correct terms
    new_content = content
    new_content = new_content.replace("时长与帧率", "时长与分辨率")
    new_content = new_content.replace("时长和帧率", "时长和分辨率")
    new_content = new_content.replace("时长、帧率", "时长、分辨率")
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully fixed '帧率' in {file_path}")
    else:
        print(f"No '帧率' mismatch found in {file_path}")

def main():
    path_orig = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    
    fix_file(path_orig)
    fix_file(path_txt)

if __name__ == "__main__":
    main()
