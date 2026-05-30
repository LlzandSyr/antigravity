import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    brain_dir = r"C:\Users\86135\.gemini\antigravity\brain"
    for cid in os.listdir(brain_dir):
        path_log = os.path.join(brain_dir, cid, ".system_generated", "logs", "overview.txt")
        if os.path.exists(path_log):
            with open(path_log, "r", encoding="utf-8") as f:
                for line in f:
                    if "Adobe Stock" in line and ("1.2" in line or "国内外研究" in line) and "replace" in line:
                        try:
                            data = json.loads(line)
                            # Find if we can extract untruncated content or see details
                            print(f"FOUND match in CID: {cid}, Step {data.get('step_index')}")
                            # Let's search if the model text had a clean snippet
                        except Exception:
                            pass

if __name__ == "__main__":
    main()
