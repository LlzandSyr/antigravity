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
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                args = tc.get("args", {})
                content_str = json.dumps(args, ensure_ascii=False)
                if "测试用例" in content_str or "表5" in content_str or "表6.1" in content_str:
                    print(f"=== Step {step} - Tool {tc['name']} ===")
                    print(f"Description: {args.get('Description')}")
                    # Print first 200 chars of ReplacementContent/TargetContent
                    for k in ["ReplacementContent", "TargetContent", "CodeContent"]:
                        if k in args:
                            val = str(args[k])
                            print(f"  {k} (len={len(val)}):\n{val[:500]}")
                    print("="*60)

if __name__ == "__main__":
    main()
