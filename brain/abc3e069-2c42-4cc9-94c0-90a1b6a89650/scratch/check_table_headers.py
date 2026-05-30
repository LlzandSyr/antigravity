import os

def main():
    path_tables = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\extracted_tables.txt"
    if not os.path.exists(path_tables):
        print("extracted_tables.txt not found")
        return
        
    with open(path_tables, "r", encoding="utf-8") as f:
        content = f.read()
        
    print("=== Table 1 raw content in extracted_tables.txt ===")
    idx = content.find("table_0")
    if idx != -1:
        print(content[idx:idx+800])
    else:
        print("table_0 not found")

if __name__ == "__main__":
    main()
