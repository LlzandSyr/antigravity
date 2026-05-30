import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    if not os.path.exists(path_log):
        print("Log not found")
        return
        
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except Exception:
                continue
                
            text = json.dumps(data, ensure_ascii=False)
            if "致谢" in text or "致  谢" in text:
                print(f"Found in Step {data.get('step_index')}:")
                # Print a snippet
                print(text[:400])
                print("-" * 40)

if __name__ == "__main__":
    main()
