import os
import zipfile
import xml.etree.ElementTree as ET

def read_docx_text(file_path):
    if not os.path.exists(file_path):
        return f"File {file_path} not found"
    try:
        # Extract text from docx without using external python-docx library to ensure compatibility
        docx = zipfile.ZipFile(file_path)
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        # Word XML namespaces
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        paragraphs = []
        for p in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
            if texts:
                paragraphs.append(''.join(texts))
        return '\n'.join(paragraphs)
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"

paths = [
    r"c:\Users\86135\Desktop\面试题\阶段项目2\FluxCloud_V2.0_项目功能逐条复盘（含AI扩展）.docx",
    r"c:\Users\86135\Desktop\面试题\阶段项目3\Aura_V2.0_项目功能逐条复盘（含AI扩展）.docx"
]

out_txt_path = r"C:\Users\86135\.gemini\antigravity\brain\d8c67ea2-5201-45be-b279-f1f8a1e5ec1b\scratch\docx_text.txt"

with open(out_txt_path, "w", encoding="utf-8") as f:
    for path in paths:
        f.write(f"=== File: {os.path.basename(path)} ===\n")
        f.write(read_docx_text(path))
        f.write("\n\n")

print("Done")
