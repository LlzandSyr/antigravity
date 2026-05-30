import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    if not os.path.exists(path_log):
        print("Log not found")
        return
        
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except Exception:
                continue
                
            step = data.get("step_index")
            if 600 <= step <= 650:
                tool_calls = data.get("tool_calls", [])
                for tc in tool_calls:
                    args = tc.get("args", {})
                    rep = args.get("ReplacementContent") or args.get("CodeContent")
                    if rep and ("总结与展望" in rep or "uni-app" in rep):
                        print(f"=== Found Chapter 7 at Step {step} ===")
                        path_out = os.path.join(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch", f"exact_ch7_step_{step}.txt")
                        with open(path_out, "w", encoding="utf-8") as out:
                            out.write(rep)
                        print(f"Successfully wrote Step {step} Chapter 7 text to {path_out}")

if __name__ == "__main__":
    main()
