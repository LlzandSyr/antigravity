import os

def main():
    path_log = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\.system_generated\logs\overview.txt"
    with open(path_log, "r", encoding="utf-8") as f:
        for line in f:
            if "Adobe Stock" in line and "replace_file_content" in line:
                print("Found match in raw line:")
                print(line[:1000])
                print("-" * 50)
                print(line[-1000:])
                print("=" * 80)

if __name__ == "__main__":
    main()
