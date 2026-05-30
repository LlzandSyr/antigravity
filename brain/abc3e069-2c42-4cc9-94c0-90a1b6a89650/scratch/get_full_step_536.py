import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    for line in lines:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except Exception:
            continue
            
        step = data.get("step_index")
        if step == 536 or step == 568:
            print(f"=== STEP {step} ===")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            print("=" * 80)

if __name__ == "__main__":
    main()
