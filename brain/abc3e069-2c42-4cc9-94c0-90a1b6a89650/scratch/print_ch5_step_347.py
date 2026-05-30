import os
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    path = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\exact_ch5_step_347.txt"
    if not os.path.exists(path):
        print("File not found")
        return
    with open(path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            print(f"{idx+1}: {line}", end="")
            
if __name__ == "__main__":
    main()
