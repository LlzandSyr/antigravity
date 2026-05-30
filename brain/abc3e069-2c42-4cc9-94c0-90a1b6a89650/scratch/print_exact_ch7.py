import os
import sys

def print_file(path, label):
    if not os.path.exists(path):
        print(f"{label} not found")
        return
    print(f"=== {label} ===")
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())
    print("="*60)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    print_file(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\exact_ch7_step_621.txt", "Step 621")
    print_file(r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\exact_ch7_step_636.txt", "Step 636")

if __name__ == "__main__":
    main()
