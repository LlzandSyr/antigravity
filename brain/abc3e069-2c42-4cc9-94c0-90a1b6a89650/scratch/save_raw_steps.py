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
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    args = tc.get("args", {})
                    rep = args.get("ReplacementContent")
                    if rep:
                        # Write directly using raw bytes representation to avoid console truncation or encode/decode issues
                        path_out = os.path.join(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch", f"raw_step_{step}.txt")
                        with open(path_out, "w", encoding="utf-8") as out:
                            out.write(rep)
                        print(f"Wrote Step {step} raw data of length {len(rep)} to {path_out}")

if __name__ == "__main__":
    main()
