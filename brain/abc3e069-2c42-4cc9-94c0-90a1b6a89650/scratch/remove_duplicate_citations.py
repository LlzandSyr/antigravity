import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Let's perform precise, unique string replacements
    
    # 1. Remove the second [1] in Paragraph 1 of 引言
    target_1 = "等高维参数[1]。"
    replacement_1 = "等高维参数。"
    if target_1 in content:
        content = content.replace(target_1, replacement_1)
        print("Replaced second [1] successfully!")
    else:
        print("Error: Target 1 not found")
        
    # 2. Remove the second [2] in Paragraph 1 of 引言
    target_2 = "多模态AI图库系统[2]，"
    replacement_2 = "多模态AI图库系统，"
    if target_2 in content:
        content = content.replace(target_2, replacement_2)
        print("Replaced second [2] successfully!")
    else:
        print("Error: Target 2 not found")
        
    # 3. Remove the duplicate [1] in Section 1.1
    target_3 = "已成为行业关注重点[1]。"
    replacement_3 = "已成为行业关注重点。"
    if target_3 in content:
        content = content.replace(target_3, replacement_3)
        print("Replaced third [1] successfully!")
    else:
        print("Error: Target 3 not found")
        
    # 4. Remove the duplicate [4] in Section 1.1
    target_4 = "提供了参考[4]。"
    replacement_4 = "提供了参考。"
    if target_4 in content:
        content = content.replace(target_4, replacement_4)
        print("Replaced second [4] successfully!")
    else:
        print("Error: Target 4 not found")
        
    # Write back to disk
    with open(path_txt, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(content)
    print("All duplicate citations removed and manuscript updated!")

if __name__ == "__main__":
    main()
