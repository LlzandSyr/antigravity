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
                if 1300 <= step < 1400:
                    print(f"Step: {step}, Role: {data.get('role')}, Type: {data.get('type')}")
                    content = data.get('content', '')
                    if content:
                        print(f"  Snippet: {content[:300]}")
                        print("." * 30)
            except Exception:
                pass

if __name__ == "__main__":
    main()
