import os

def main():
    path = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\thesis_polishing_accomplishment.md"
    if not os.path.exists(path):
        print("thesis_polishing_accomplishment.md not found")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "致谢" in content or "致  谢" in content:
        print("Found in thesis_polishing_accomplishment.md!")
        idx = content.find("致谢")
        if idx == -1:
            idx = content.find("致  谢")
        print(content[max(0, idx-100):idx+300])
    else:
        print("Not found in thesis_polishing_accomplishment.md")

if __name__ == "__main__":
    main()
