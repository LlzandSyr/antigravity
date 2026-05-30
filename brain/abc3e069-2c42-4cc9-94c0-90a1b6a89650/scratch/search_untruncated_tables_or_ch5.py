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
            # We look for ANY tool call that did a successful replacement in manuscript-v4 or v3
            # and print the actual arguments if they contain larger text (e.g. not truncated)
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                args = tc.get("args", {})
                desc = args.get("Description", "")
                if "Refactor Chapter 5" in desc or "Table 1-4" in desc or "Table 5-9" in desc:
                    print(f"=== Step {step} ===")
                    print(f"Description: {desc}")
                    print(f"Keys: {list(args.keys())}")
                    for k, v in args.items():
                        if isinstance(v, str) and len(v) > 200:
                            print(f"{k} (len={len(v)}):\n{v[:400]}")
                            print("...")
                    print("=" * 60)

if __name__ == "__main__":
    main()
