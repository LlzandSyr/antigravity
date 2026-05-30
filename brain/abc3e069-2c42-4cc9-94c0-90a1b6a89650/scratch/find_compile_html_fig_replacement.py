import os

def main():
    path_compile = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\compile_html_v2.py"
    if not os.path.exists(path_compile):
        print("compile_html_v2.py not found")
        return
        
    with open(path_compile, "r", encoding="utf-8") as f:
        content = f.read()
        
    print("=== Figure replacements in compile_html_v2.py ===")
    idx = 0
    while True:
        idx = content.find("图", idx)
        if idx == -1:
            break
        print(content[max(0, idx-50):min(len(content), idx+100)])
        print("-" * 50)
        idx += 1

if __name__ == "__main__":
    main()
