import os
import json

def main():
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("step_index") == 325:
                    tool_calls = data.get("tool_calls", [])
                    for tc in tool_calls:
                        args = tc.get("args", {})
                        # Save the raw contents into files so we can read them directly without print limits
                        with open(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\step_325_target.txt", "w", encoding="utf-8") as f_out:
                            f_out.write(args.get("TargetContent", ""))
                        with open(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\step_325_replacement.txt", "w", encoding="utf-8") as f_out:
                            f_out.write(args.get("ReplacementContent", ""))
                        print("Successfully wrote untruncated contents to scratch!")
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
