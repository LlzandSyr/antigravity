import os

p3_base = r"c:\Users\86135\Desktop\面试题\阶段项目3\李怜哲+微光智控餐饮终端\Aura_Client"
files = [
    os.path.join(p3_base, "menumodel.h"),
    os.path.join(p3_base, "menumodel.cpp"),
    os.path.join(p3_base, "menudelegate.h"),
    os.path.join(p3_base, "menudelegate.cpp")
]

for filepath in files:
    if os.path.exists(filepath):
        print(f"File: {os.path.basename(filepath)}")
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f):
                if "changeQty" in line:
                    print(f"  Line {i+1}: {line.strip()}")
