import re

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i in range(len(lines) - 1):
        line1 = lines[i].rstrip('\n')
        line2 = lines[i+1].rstrip('\n')
        if not line1 or not line2:
            continue
        
        last_char = line1[-1] if line1 else ''
        first_char = line2.lstrip()[0] if line2.lstrip() else ''
        
        if re.match(r'[A-Za-z0-9]', last_char) and re.match(r'[A-Za-z0-9]', first_char):
            print(f"Line {i+1} ends with '{last_char}', Line {i+2} starts with '{first_char}':")
            print(f"  Line {i+1}: {line1}")
            print(f"  Line {i+2}: {line2}")

if __name__ == "__main__":
    main()
