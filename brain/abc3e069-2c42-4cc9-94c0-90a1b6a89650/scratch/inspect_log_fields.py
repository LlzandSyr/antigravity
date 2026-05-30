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
            if step in [340, 443]:
                print(f"=== STEP {step} keys ===")
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    print(f"Tool: {tc['name']}")
                    args = tc.get("args", {})
                    for k, v in args.items():
                        if isinstance(v, str):
                            print(f"Arg {k}: type={type(v)}, len={len(v)}, repr={repr(v[:100])}")
                        else:
                            print(f"Arg {k}: type={type(v)}")

if __name__ == "__main__":
    main()
