import re

filepath = r"C:\Users\86135\Gemini\antigravity\brain\d8c67ea2-5201-45be-b279-f1f8a1e5ec1b\scratch\docx_text.txt"
# Wait, let's use the absolute path we read before
filepath = r"C:\Users\86135\.gemini\antigravity\brain\d8c67ea2-5201-45be-b279-f1f8a1e5ec1b\scratch\docx_text.txt"

with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Look for placeholders
print("=== Brackets Search ===")
brackets = re.findall(r"【[^】]*】", text)
for b in set(brackets):
    print(f"Found placeholder: {b}")

print("\n=== TODO / Incomplete markers ===")
lines = text.split("\n")
for i, line in enumerate(lines):
    if "TODO" in line or "待" in line or "根据实际" in line:
        print(f"Line {i+1}: {line}")
