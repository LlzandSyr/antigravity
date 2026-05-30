import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except Exception:
                continue
                
            step = data.get("step_index")
            if step == 1340:
                print("=== Step 1340 ===")
                text = json.dumps(data, ensure_ascii=False)
                # print first 2000 chars of step 1340 content
                content = data.get("content", "")
                print(content[:2000])
                print("="*60)

if __name__ == "__main__":
    main()
