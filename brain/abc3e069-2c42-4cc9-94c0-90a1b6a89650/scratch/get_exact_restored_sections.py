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
        content = f.read()
        
    lines = content.split('\n')
    
    # Search for model replacement text between step 330 and step 460
    for idx, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except Exception:
            continue
            
        step = data.get("step_index")
        if 330 <= step <= 460:
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                args = tc.get("args", {})
                content_str = json.dumps(args, ensure_ascii=False)
                if "实现" in content_str or "表" in content_str or "测试" in content_str:
                    print(f"=== Step {step} - Tool {tc['name']} ===")
                    print(f"Description: {args.get('Description')}")
                    if "ReplacementContent" in args:
                        print(args["ReplacementContent"][:500])
                    elif "ReplacementChunks" in args:
                        for chunk in args["ReplacementChunks"]:
                            print(f"Chunk StartLine: {chunk.get('StartLine')}, EndLine: {chunk.get('EndLine')}")
                            print(chunk.get("ReplacementContent")[:300])
                    print("=" * 60)

if __name__ == "__main__":
    main()
