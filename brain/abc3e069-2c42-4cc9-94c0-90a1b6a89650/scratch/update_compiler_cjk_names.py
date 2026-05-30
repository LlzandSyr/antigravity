import os

def main():
    path_compiler = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch\compile_html_clean.py"
    if not os.path.exists(path_compiler):
        print("Compiler not found")
        return
        
    code = """import os
import re

def main():
    path_txt = r"C:\\Users\\86135\\Desktop\\优秀毕业论文\\稿件-v4.txt"
    path_html = r"C:\\Users\\86135\\Desktop\\优秀毕业论文\\稿件.html"
    
    if not os.path.exists(path_txt):
        print(f"Error: {path_txt} not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Standardize line endings and split
    lines = content.splitlines()
    
    html_lines = []
    
    # HTML Header with default/fallback styles
    html_lines.append(\"\"\"<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>基于Spring Boot+Vue的多模态AI图库系统的设计与实现</title>
<style>
  @page {
    size: A4;
    margin-top: 28mm;
    margin-bottom: 22mm;
    margin-left: 30mm;
    margin-right: 20mm;
  }
  body {
    font-family: 'Times New Roman', '宋体', 'SimSun', serif;
    background-color: #ffffff;
    color: #000000;
    margin: 0;
    padding: 0;
    line-height: 20pt;
  }
  .container {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
  }
</style>
</head>
<body>
<div class="container">
\"\"\")

    for idx, raw_line in enumerate(lines):
        line = raw_line.strip()
        if not line:
            continue
            
        # Title (First line): 3号黑体加粗居中 -> 16pt, English Times New Roman, Chinese 黑体
        if idx == 0:
            html_lines.append(f'  <h1 style="font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 16pt; font-weight: bold; text-align: center; line-height: 20pt; margin-bottom: 12pt;">{line}</h1>')
            continue
            
        # Authors / Metadata (Line 3): 小四号楷体居中 -> 12pt, English Times New Roman, Chinese 楷体
        if idx == 2:
            html_lines.append(f'  <div style="font-family: \\'Times New Roman\\', \\'楷体\\', \\'KaiTi\\', \\'STKaiti\\', serif; mso-fareast-font-family: \\'楷体\\'; font-size: 12pt; text-align: center; line-height: 20pt; margin-bottom: 24pt;">{line}</div>')
            continue
            
        # Abstract box: label is 12pt 黑体, text is 10.5pt 楷体
        if line.startswith("摘要："):
            abstract_text = line[3:].strip()
            html_lines.append(f'  <p style="text-indent: 2em; font-family: \\'Times New Roman\\', \\'楷体\\', \\'KaiTi\\', \\'STKaiti\\', serif; mso-fareast-font-family: \\'楷体\\'; font-size: 10.5pt; line-height: 20pt; text-align: justify; margin: 0 0 6pt 0;"><strong style="font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 12pt; font-weight: bold;">摘要：</strong>{abstract_text}</p>')
            continue
            
        # Keywords box: label is 12pt 黑体, text is 10.5pt 楷体
        if line.startswith("关键词："):
            keywords_text = line[4:].strip()
            html_lines.append(f'  <p style="text-indent: 2em; font-family: \\'Times New Roman\\', \\'楷体\\', \\'KaiTi\\', \\'STKaiti\\', serif; mso-fareast-font-family: \\'楷体\\'; font-size: 10.5pt; line-height: 20pt; text-align: justify; margin: 0 0 18pt 0;"><strong style="font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 12pt; font-weight: bold;">关键词：</strong>{keywords_text}</p>')
            continue
            
        # Table captions (centered, 10.5pt 黑体 bold)
        if re.match(r'^表\d+\s+', line):
            html_lines.append(f'  <p style="text-indent: 0; font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 10.5pt; font-weight: bold; text-align: center; margin: 12pt 0 6pt 0; line-height: 20pt;">{line}</p>')
            continue
            
        # Figure captions (centered, 10.5pt 黑体 bold)
        if re.match(r'^图\d+\s+', line):
            html_lines.append(f'  <p style="text-indent: 0; font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 10.5pt; font-weight: bold; text-align: center; margin: 6pt 0 12pt 0; line-height: 20pt;">{line}</p>')
            continue
            
        # References section header (un-numbered, centered 14pt 黑体)
        if "".join(line.split()) == "参考文献":
            html_lines.append(f'  <h1 style="font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 14pt; font-weight: bold; text-align: center; margin-top: 24pt; margin-bottom: 12pt; line-height: 20pt;">参  考  文  献</h1>')
            continue
            
        # Reference item matching [1], [2], etc. (hanging indent 2em, 10.5pt 宋体)
        if re.match(r'^\[\d+\]\s+', line):
            html_lines.append(f'  <p style="text-indent: -2em; padding-left: 2em; font-family: \\'Times New Roman\\', \\'宋体\\', \\'SimSun\\', serif; mso-fareast-font-family: \\'宋体\\'; font-size: 10.5pt; line-height: 20pt; text-align: justify; margin: 0 0 6pt 0;">{line}</p>')
            continue
            
        # English section Title (3号 Times New Roman, bold, centered -> 16pt)
        if line.startswith("Design and Implementation of a Multimodal AI"):
            html_lines.append(f'  <h1 style="font-family: \\'Times New Roman\\', serif; mso-fareast-font-family: \\'Times New Roman\\'; font-size: 16pt; font-weight: bold; text-align: center; line-height: 20pt; margin-top: 36pt; margin-bottom: 12pt;">{line}</h1>')
            continue
            
        # English section Abstract (小四 Times New Roman, bold label, 12pt text)
        if line.startswith("Abstract:"):
            eng_abs = line[9:].strip()
            html_lines.append(f'  <p style="text-indent: 2em; font-family: \\'Times New Roman\\', serif; mso-fareast-font-family: \\'Times New Roman\\'; font-size: 12pt; line-height: 20pt; text-align: justify; margin: 0 0 6pt 0;"><strong style="font-family: \\'Times New Roman\\', serif; mso-fareast-font-family: \\'Times New Roman\\'; font-size: 12pt; font-weight: bold;">Abstract: </strong>{eng_abs}</p>')
            continue
            
        # English section Keywords (小四 Times New Roman, bold label, 12pt text)
        if line.startswith("Keywords:") or line.startswith("Key Words:"):
            prefix_len = 9 if line.startswith("Keywords:") else 10
            eng_kw = line[prefix_len:].strip()
            html_lines.append(f'  <p style="text-indent: 2em; font-family: \\'Times New Roman\\', serif; mso-fareast-font-family: \\'Times New Roman\\'; font-size: 12pt; line-height: 20pt; text-align: justify; margin: 0 0 6pt 0;"><strong style="font-family: \\'Times New Roman\\', serif; mso-fareast-font-family: \\'Times New Roman\\'; font-size: 12pt; font-weight: bold;">Key Words: </strong>{eng_kw}</p>')
            continue
            
        # Headings (Level 1, 2, 3)
        heading_match = re.match(r'^(\d+(\.\d+)*)\s+(.*)', line)
        if heading_match:
            num = heading_match.group(1)
            level = len(num.split('.'))
            text = heading_match.group(3).strip()
            
            if level == 1:
                # 4号黑体 -> 14pt
                html_lines.append(f'  <h1 style="font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 14pt; font-weight: bold; line-height: 20pt; margin-top: 24pt; margin-bottom: 12pt; text-align: left;">{num}  {text}</h1>')
            elif level == 2:
                # 小4号黑体 -> 12pt
                html_lines.append(f'  <h2 style="font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 12pt; font-weight: bold; line-height: 20pt; margin-top: 18pt; margin-bottom: 9pt; text-align: left;">{num}  {text}</h2>')
            else:
                # 小4号黑体 -> 12pt
                html_lines.append(f'  <h3 style="font-family: \\'Times New Roman\\', \\'黑体\\', \\'SimHei\\', sans-serif; mso-fareast-font-family: \\'黑体\\'; font-size: 12pt; font-weight: bold; line-height: 20pt; margin-top: 12pt; margin-bottom: 6pt; text-align: left;">{num}  {text}</h3>')
            continue
            
        # Standard paragraph (5号宋体/Times New Roman -> 10.5pt)
        clean_text = raw_line.lstrip('　').lstrip()
        html_lines.append(f'  <p style="text-indent: 2em; font-family: \\'Times New Roman\\', \\'宋体\\', \\'SimSun\\', serif; mso-fareast-font-family: \\'宋体\\'; font-size: 10.5pt; line-height: 20pt; text-align: justify; margin: 0 0 6pt 0;">{clean_text}</p>')

    # HTML Footer
    html_lines.append(\"\"\"</div>
</body>
</html>
\"\"\")

    with open(path_html, "w", encoding="utf-8") as out:
        out.write("\\n".join(html_lines))
        
    print(f"Successfully generated 100% clean, exact matching HTML manuscript at {path_html}")

if __name__ == "__main__":
    main()
"""
    with open(path_compiler, "w", encoding="utf-8") as f:
        f.write(code)
    print("Successfully updated compile_html_clean.py with multi-fallback font stacks!")

if __name__ == "__main__":
    main()
