import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step = data.get("step_index")
                if 310 <= step <= 330:
                    tool_calls = data.get("tool_calls", [])
                    if tool_calls:
                        print(f"=== Tool calls in Step {step} ===")
                        for tc in tool_calls:
                            print(tc.get("name"))
                            print(json.dumps(tc.get("args"), indent=2, ensure_ascii=False))
                            print("-" * 30)
            except Exception:
                pass

if __name__ == "__main__":
    main()
