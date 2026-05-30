import os

def main():
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    if not os.path.exists(path_log):
        print("Log not found")
        return
        
    with open(path_log, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    print(f"Log total lines: {len(lines)}")
    
    # Print lines containing "springboot" or "vue" or "减少" or "技术介绍"
    for i, line in enumerate(lines):
        if "springboot" in line.lower() or "vue" in line.lower() or "技术介绍" in line or "相关技术" in line or "减少" in line or "保留" in line:
            print(f"Line {i+1}: {line.strip()[:150]}")

if __name__ == "__main__":
    main()
