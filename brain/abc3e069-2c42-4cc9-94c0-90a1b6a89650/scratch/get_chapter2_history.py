import os
import sys

def main():
    # Set stdout to utf-8 to avoid console printing issues on windows
    sys.stdout.reconfigure(encoding='utf-8')
    
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    print(f"Total lines: {len(lines)}")
    
    # We want to print any model edits or user requests regarding Chapter 2 or technology introduction
    # starting from line 200
    for idx in range(200, len(lines)):
        line = lines[idx]
        if "replace_file_content" in line or "multi_replace_file_content" in line or "L126-L195" in line or "技术" in line or "vue" in line.lower() or "springboot" in line.lower():
            # Print index + 1 and the line
            print(f"Line {idx+1}: {line[:300]}")

if __name__ == "__main__":
    main()
