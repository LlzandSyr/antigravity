import os
import json

def main():
    path_txt = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\best_ch5_step_347.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        val = f.read()
    # It starts and ends with double quotes, it is a JSON string
    try:
        text = json.loads(val)
        print("=== Step 347 Chapter 5 (Length={}) ===".format(len(text)))
        print(text)
    except Exception as e:
        print("JSON decode failed, raw print first 500 chars:")
        print(val[:500])

if __name__ == "__main__":
    main()
