import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("=== Final Headings in HTML ===")
    for idx, l in enumerate(lines):
        if "5.2.1" in l or "5.2.2" in l or "5.2.3" in l or "5.2.4" in l or "5.2.5" in l:
            # Print the heading line and the next 2 lines (which should be empty or paragraph)
            print(f"--- Heading Line {idx+1} ---")
            for j in range(idx, min(len(lines), idx+4)):
                print(f"{j+1}: {lines[j].strip()}")

if __name__ == "__main__":
    main()
