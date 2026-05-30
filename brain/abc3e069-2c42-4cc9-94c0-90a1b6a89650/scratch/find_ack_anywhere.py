import os
import glob

def main():
    paths_to_search = [
        r"C:\Users\86135\Desktop\优秀毕业论文",
        r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650"
    ]
    
    print("=== Deep search for '致谢' or '致  谢' ===")
    for folder in paths_to_search:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if any(ext in file.lower() for ext in [".txt", ".html", ".md", ".py"]):
                    path = os.path.join(root, file)
                    for enc in ["utf-8", "gbk", "gb18030"]:
                        try:
                            with open(path, "r", encoding=enc) as f:
                                content = f.read()
                            if "致谢" in content or "致  谢" in content:
                                print(f"Found in: {path} (encoding {enc})")
                                # Print surrounding text
                                idx = content.find("致谢")
                                if idx == -1:
                                    idx = content.find("致  谢")
                                print(content[max(0, idx-100):idx+300])
                                print("-" * 40)
                                break
                        except Exception:
                            pass

if __name__ == "__main__":
    main()
