text_file = r"C:\Users\86135\.gemini\antigravity\brain\d8c67ea2-5201-45be-b279-f1f8a1e5ec1b\scratch\docx_text.txt"

with open(text_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith("=== ") or line.startswith("一、") or line.startswith("二、") or line.startswith("三、") or line.startswith("四、") or line.startswith("五、") or "复盘" in line or "核心" in line:
        print(f"Line {i+1}: {line.strip()}")
