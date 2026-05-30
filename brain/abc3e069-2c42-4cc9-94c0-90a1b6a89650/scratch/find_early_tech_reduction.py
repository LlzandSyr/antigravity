import os
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    if not os.path.exists(path_log):
        print("Log not found")
        return
        
    with open(path_log, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    print("=== Searching early logs (1 to 200) ===")
    for i in range(min(200, len(lines))):
        line = lines[i]
        if "springboot" in line.lower() or "vue" in line.lower() or "技术" in line or "两项" in line or "保留" in line:
            print(f"Line {i+1}: {line[:200]}")

if __name__ == "__main__":
    main()
