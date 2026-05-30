import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Print the last 10 lines
    print("=== Last 10 log lines ===")
    for line in lines[-10:]:
        try:
            data = json.loads(line)
            print(f"Step: {data.get('step_index')}, Role: {data.get('role')}, Type: {data.get('type')}")
            content = data.get('content', '')
            if content:
                print(f"  Snippet: {content[:300]}")
        except Exception as e:
            print(f"Error parsing line: {e}")

if __name__ == "__main__":
    main()
