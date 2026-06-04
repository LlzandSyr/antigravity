import os

text_file = r"C:\Users\86135\.gemini\antigravity\brain\d8c67ea2-5201-45be-b279-f1f8a1e5ec1b\scratch\docx_text.txt"
output_file = r"C:\Users\86135\.gemini\antigravity\brain\d8c67ea2-5201-45be-b279-f1f8a1e5ec1b\scratch\found_todos.txt"

with open(text_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

todos = []
for i, line in enumerate(lines):
    # Check for Chinese words for "todo", "incomplete", "verify", "actual", etc.
    # also check for bracket structures, "TODO", etc.
    if any(w in line for w in ["TODO", "todo", "待", "暂无", "需要根据", "实际", "补充", "纠正", "纠错", "错误"]):
        todos.append(f"Line {i+1}: {line.strip()}")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(todos))

print(f"Wrote {len(todos)} lines to found_todos.txt")
