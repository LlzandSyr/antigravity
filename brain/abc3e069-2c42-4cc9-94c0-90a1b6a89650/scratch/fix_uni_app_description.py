import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace target string
    target = "项目同步研发了基于uni-app的跨端移动应用（如pixelhub-uni-app-dev），完成了针对移动终端的适配与多端编译，实现了移动端资产预览、智能创作与协同空间的敏捷管理，满足了多终端无缝流转的工程要求。"
    replacement = "项目同步研发了基于uni-app的跨端移动应用，由于篇幅有限，本论文未对移动端相关规范进行具体描述；该移动端应用完成了针对移动终端的适配与多端编译，实现了移动端资产预览、智能创作与协同空间的敏捷管理，满足了多终端无缝流转的工程要求。"
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(path_txt, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated uni-app description in 稿件-v4.txt")
    else:
        print("Target string not found in 稿件-v4.txt")
        # Try to find part of it
        if "pixelhub-uni-app-dev" in content:
            print("Found pixelhub-uni-app-dev, let's do a line-by-line replacement")
            lines = content.splitlines()
            for idx, l in enumerate(lines):
                if "pixelhub-uni-app-dev" in l:
                    print(f"Original Line {idx+1}: {l[:100]}...")
                    lines[idx] = l.replace("（如pixelhub-uni-app-dev）", "，由于篇幅有限，本论文未对移动端相关规范进行具体描述；")
            with open(path_txt, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print("Successfully updated uni-app description line-by-line")

if __name__ == "__main__":
    main()
