import os
import json

def main():
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("step_index") == 1400:
                    content = data.get("content", "")
                    if "致谢" in content or "致  谢" in content:
                        print("Yes, found '致谢' in Step 1400 content!")
                    else:
                        print("No '致谢' in Step 1400 content.")
            except Exception:
                pass

if __name__ == "__main__":
    main()
