import os
import json
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    # We look for steps 536, 547, 550, 553, 559
    target_steps = [536, 547, 550, 553, 559, 568, 574, 583]
    for idx, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except Exception:
            continue
            
        step = data.get("step_index")
        if step in target_steps:
            print(f"=== Step {step} ===")
            # Pretty print the tool call or the response
            tool_calls = data.get("tool_calls")
            if tool_calls:
                for tc in tool_calls:
                    print(f"Tool Call: {tc['name']}")
                    args = tc.get("args", {})
                    # Print target content or replacement content
                    if "ReplacementContent" in args:
                        print(f"ReplacementContent:\n{args['ReplacementContent']}")
                    elif "replacementContent" in args:
                        print(f"replacementContent:\n{args['replacementContent']}")
                    elif "ReplacementChunks" in args:
                        for chunk in args["ReplacementChunks"]:
                            print(f"Chunk Target:\n{chunk.get('TargetContent')}")
                            print(f"Chunk Replacement:\n{chunk.get('ReplacementContent')}")
                    else:
                        print(f"Args: {json.dumps(args, indent=2, ensure_ascii=False)}")
            else:
                print(f"Response: {data.get('content', '')[:1000]}")
            print("=" * 60)

if __name__ == "__main__":
    main()
