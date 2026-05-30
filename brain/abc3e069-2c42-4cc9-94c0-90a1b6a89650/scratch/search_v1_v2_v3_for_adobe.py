import os

def main():
    folder = r"C:\Users\86135\Desktop\优秀毕业论文"
    files = ["稿件-v1.txt", "稿件-v2.txt", "稿件-v3.txt"]
    for file in files:
        path = os.path.join(folder, file)
        if not os.path.exists(path):
            print(f"Not found: {file}")
            continue
        print(f"Reading: {file}")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Adobe" in content or "adobe" in content.lower():
            print(f"FOUND 'Adobe' in {file}!")
            idx = content.lower().find("adobe")
            print(content[max(0, idx-100):idx+300])
            print("=" * 60)
        else:
            print(f"Not found in {file}")

if __name__ == "__main__":
    main()
