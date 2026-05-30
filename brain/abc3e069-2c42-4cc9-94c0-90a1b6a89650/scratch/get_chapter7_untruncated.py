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
                
            step = data.get("step_index")
            if step == 636 or step == 642:
                print(f"=== STEP {step} ===")
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    args = tc.get("args", {})
                    rep = args.get("ReplacementContent")
                    if rep:
                        print(rep)
                print("=" * 80)

if __name__ == "__main__":
    main()
