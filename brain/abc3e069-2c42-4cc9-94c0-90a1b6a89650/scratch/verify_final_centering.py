import os

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    if not os.path.exists(path_html):
        print("HTML not found")
        return
        
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"File Size: {os.path.getsize(path_html)} bytes")
    
    # Check centered table count
    tables_centered = content.count('<table align="center"')
    print(f"Centered Tables: {tables_centered}")
    
    # Check figure placeholders count
    placeholders = content.count('截图占位符')
    print(f"Figure Placeholders: {placeholders}")
    
    # Check if table caption contains "text-align: center"
    table_captions_centered = content.count('text-align: center; margin: 12pt 0 6pt 0;')
    print(f"Centered Table Captions: {table_captions_centered}")
    
    # Check if figure caption contains "text-align: center"
    fig_captions_centered = content.count('text-align: center; margin: 6pt 0 12pt 0;')
    print(f"Centered Figure Captions: {fig_captions_centered}")

if __name__ == "__main__":
    main()
