import os
import re

def main():
    path_main = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    if not os.path.exists(path_main):
        print("Main thesis file not found")
        return
        
    with open(path_main, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Search for "6.3" and see what text is after it
    # We can search with regex "##\s*6\.3\s" or "6.3\s"
    matches = [m.start() for m in re.finditer(r"6\.3\s+", content)]
    for idx, start in enumerate(matches):
        print(f"=== Match {idx} ===")
        print(content[start:start+1000])
        print("="*60)
        
    # Also search for "4.3" or "逻辑结构"
    matches_43 = [m.start() for m in re.finditer(r"4\.3\s+", content)]
    for idx, start in enumerate(matches_43):
        print(f"=== Match 4.3 {idx} ===")
        print(content[start:start+1000])
        print("="*60)

if __name__ == "__main__":
    main()
