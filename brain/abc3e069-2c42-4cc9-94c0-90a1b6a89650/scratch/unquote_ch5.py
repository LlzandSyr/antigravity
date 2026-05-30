import os
import json

def unescape_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Try parsing as JSON first
    try:
        unescaped = json.loads(content)
    except Exception:
        # Fallback: replace literal \n and \"
        unescaped = content.replace("\\n", "\n").replace('\\"', '"').strip('"')
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(unescaped)
    print(f"Unescaped {path} successfully!")

def main():
    unescape_file(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\exact_ch5_step_347.txt")
    unescape_file(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\exact_ch5_step_361.txt")

if __name__ == "__main__":
    main()
