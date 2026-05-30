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
            # We look for Step 347 or Step 361 where Chapter 5 was refactored
            if step in [347, 361]:
                print(f"=== Step {step} ===")
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    args = tc.get("args", {})
                    rep = args.get("ReplacementContent")
                    if rep:
                        # Write to a file
                        path_out = os.path.join(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch", f"best_ch5_step_{step}.txt")
                        with open(path_out, "w", encoding="utf-8") as out:
                            out.write(rep)
                        print(f"Wrote Step {step} Ch5 to {path_out}, length={len(rep)}")

if __name__ == "__main__":
    main()
