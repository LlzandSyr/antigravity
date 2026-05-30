import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\档案-v4.txt" # Wait, log is overview.txt
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    if not os.path.exists(path_log):
        print("Log not found")
        return
        
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                content = data.get("content", "")
                if "Adobe Stock" in content or "Adobe" in content:
                    print(f"=== Found in Step {data.get('step_index')} ===")
                    print(content[:600])
                    print("." * 40)
            except Exception:
                pass

if __name__ == "__main__":
    main()
