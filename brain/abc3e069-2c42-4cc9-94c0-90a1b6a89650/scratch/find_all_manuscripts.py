import os
import sys

def search_files(dir_path):
    results = []
    if not os.path.exists(dir_path):
        return results
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if "稿件" in f or "v4" in f or "v3" in f:
                results.append(os.path.join(root, f))
    return results

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    desktop_dir = r"C:\Users\86135\Desktop\优秀毕业论文"
    app_data_dir = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650"
    
    all_files = search_files(desktop_dir) + search_files(app_data_dir)
    print(f"Total files found: {len(all_files)}")
    
    for filepath in all_files:
        if filepath.endswith(".txt") or filepath.endswith(".md"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
                
            idx = content.find("2  相关技术介绍")
            if idx != -1:
                # Count headings like "2.1", "2.2", "2.3", "2.4" etc. in the next 1500 chars
                sub_section = content[idx:idx+1500]
                headings = []
                for h in ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9"]:
                    if h in sub_section:
                        headings.append(h)
                print(f"File: {filepath}")
                print(f"  Headings: {headings}")
                print(f"  Snippet: {sub_section[:200].strip()}...")
                print("-" * 50)

if __name__ == "__main__":
    main()
