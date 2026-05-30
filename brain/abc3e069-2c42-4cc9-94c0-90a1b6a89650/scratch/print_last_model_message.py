import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for line in reversed(lines):
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if step < 1401 and data.get("type") in ["PLANNER_RESPONSE", "MODEL_RESPONSE", "FINAL_RESPONSE"] and data.get("content"):
                print(f"=== Found last model response at Step {step} ===")
                print(data.get("content"))
                print("="*60)
                break
        except Exception:
            pass

if __name__ == "__main__":
    main()
