def main():
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    for idx in range(185, min(240, len(lines))):
        print(f"{idx+1}: {lines[idx][:250]}")

if __name__ == "__main__":
    main()
