import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    new_lines = []
    
    for l in lines:
        stripped = l.strip()
        # Match 5.2.1 to 5.2.5 with a colon
        if stripped.startswith("5.2.") and ("：" in stripped or ":" in stripped):
            parts = stripped.split("：", 1) if "：" in stripped else stripped.split(":", 1)
            subheading = parts[0].strip()
            body_text = parts[1].strip()
            new_lines.append(subheading)
            new_lines.append("　　" + body_text)
            print(f"Splitting: {subheading} AND {body_text[:30]}...")
        else:
            new_lines.append(l)
            
    with open(path_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
        
    print("Successfully split subheadings in C:\\Users\\86135\\Desktop\\优秀毕业论文\\稿件-v4.txt")

if __name__ == "__main__":
    main()
