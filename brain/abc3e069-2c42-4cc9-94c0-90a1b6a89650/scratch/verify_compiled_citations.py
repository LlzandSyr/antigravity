import re

def main():
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    with open(path_html, "r", encoding="utf-8") as f:
        content = f.read()
        
    print("=== Verification of Compiled HTML Citations ===")
    
    # Find all paragraph tags containing citations
    paragraphs = re.findall(r'<p>.*?</p>', content)
    for p in paragraphs:
        if any(c in p for c in ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[10]"]):
            # Clean HTML tags to make it readable
            clean_p = re.sub(r'<.*?>', '', p)
            print(f"P: {clean_p[:150]}...")

if __name__ == "__main__":
    main()
