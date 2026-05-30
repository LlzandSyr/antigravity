import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    for idx, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except Exception:
            continue
            
        step = data.get("step_index")
        if step >= 530:
            content_field = data.get("content", "")
            if "Spring Boot" in content_field or "Vue" in content_field or "相关技术介绍" in content_field or "2." in content_field:
                # Print the content
                print(f"=== STEP {step} (PLANNER RESPONSE) ===")
                print(content_field)
                print("=" * 80)

if __name__ == "__main__":
    main()
