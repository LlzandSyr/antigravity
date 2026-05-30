def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"HTML File Size: {len(content)} bytes")
    
    # Check for duplicate raw table lines
    raw_pipes = content.count("|")
    print(f"Number of '|' characters in HTML: {raw_pipes}")
    
    # Print lines containing tables
    lines = content.split('\n')
    table_lines = [i+1 for i, l in enumerate(lines) if "<table" in l]
    print(f"Table start lines: {table_lines}")
    
    # Check for bibliography citations in Chapter 1
    intro_lines = [l.strip() for l in lines if "以Stable Diffusion" in l]
    print(f"Intro lines: {intro_lines}")

if __name__ == "__main__":
    main()
