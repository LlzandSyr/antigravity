import re
import os

def parse_extracted_tables(scratch_dir):
    path_tables = os.path.join(scratch_dir, "extracted_tables.txt")
    with open(path_tables, "r", encoding="utf-8") as f:
        content = f.read()
    
    blocks = content.split("=== ")
    tables_dict = {}
    for block in blocks:
        if not block.strip():
            continue
        lines = block.split("\n")
        title_line = lines[0].strip()
        title = title_line.replace(" ===", "").strip()
        
        table_lines = [l.strip() for l in lines[1:] if l.strip().startswith("|")]
        if not table_lines:
            continue
            
        tables_dict[title] = table_lines
    return tables_dict

def render_db_table(rows):
    html = ['<table style="border-collapse: collapse; border: 1px solid black; width: 100%; margin: 6pt 0 12pt 0; font-size: 10.5pt; font-family: SimSun, serif; text-align: left;">']
    headers = [col.strip() for col in rows[0].split('|')[1:-1]]
    html.append('  <tr style="font-weight: bold; background-color: #f2f2f2; text-align: center;">')
    for h in headers:
        html.append(f'    <th style="border: 1px solid black; padding: 5pt 8pt;">{h}</th>')
    html.append('  </tr>')
    for r in rows[2:]:
        cols = [col.strip() for col in r.split('|')[1:-1]]
        html.append('  <tr>')
        for c in cols:
            html.append(f'    <td style="border: 1px solid black; padding: 5pt 8pt; text-align: center;">{c}</td>')
        html.append('  </tr>')
    html.append('</table>')
    return "\n".join(html)

def render_test_table(rows, table_idx):
    case_num = f"0{table_idx - 3}"
    test_scene = ""
    test_target = ""
    for r in rows:
        if "测试场景" in r:
            parts = [p.strip() for p in r.split('|')[1:-1]]
            test_scene = parts[1]
        elif "测试对象" in r:
            parts = [p.strip() for p in r.split('|')[1:-1]]
            test_target = parts[1]
            
    html = ['<table style="border-collapse: collapse; border: 1px solid black; width: 100%; margin: 6pt 0 12pt 0; font-size: 10.5pt; font-family: SimSun, serif; text-align: left;">']
    html.append(f'  <tr>')
    html.append(f'    <td colspan="5" style="border: 1px solid black; padding: 5pt 8pt; font-weight: bold; background-color: #f2f2f2;">用例编号：{case_num} &nbsp;&nbsp;&nbsp;&nbsp; 测试场景：{test_scene} &nbsp;&nbsp;&nbsp;&nbsp; 测试对象：{test_target}</td>')
    html.append(f'  </tr>')
    
    grid_header_idx = -1
    for idx, r in enumerate(rows):
        if "序号" in r:
            grid_header_idx = idx
            break
            
    if grid_header_idx != -1:
        headers = [col.strip() for col in rows[grid_header_idx].split('|')[1:-1]]
        html.append('  <tr style="font-weight: bold; background-color: #f9f9f9; text-align: center;">')
        widths = ["8%", "25%", "37%", "22%", "8%"]
        for i, h in enumerate(headers):
            html.append(f'    <th style="border: 1px solid black; padding: 5pt 8pt; width: {widths[i]};">{h}</th>')
        html.append('  </tr>')
        for r in rows[grid_header_idx+1:]:
            cols = [col.strip() for col in r.split('|')[1:-1]]
            html.append('  <tr>')
            for i, c in enumerate(cols):
                align = "left"
                if i == 0 or i == 4:
                    align = "center"
                html.append(f'    <td style="border: 1px solid black; padding: 5pt 8pt; text-align: {align};">{c}</td>')
            html.append('  </tr>')
    html.append('</table>')
    return "\n".join(html)

def main():
    scratch_dir = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch"
    tables_dict = parse_extracted_tables(scratch_dir)
    
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    html_lines = []
    
    # Document Meta Header
    html_lines.append("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>基于Spring Boot与Vue的多模态AI图库系统的设计与实现</title>
<style>
  @page {
    size: A4;
    margin-top: 28mm;
    margin-bottom: 22mm;
    margin-left: 30mm;
    margin-right: 20mm;
  }
  body {
    font-family: 'Times New Roman', 'SimSun', serif;
    background-color: #ffffff;
    color: #000000;
    margin: 0;
    padding: 0;
  }
  .container {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
  }
  h1.title {
    font-family: SimHei, sans-serif;
    font-size: 16pt;
    font-weight: bold;
    text-align: center;
    line-height: 24pt;
    margin-bottom: 12pt;
  }
  .authors {
    font-family: KaiTi, STKaiti, serif;
    font-size: 12pt;
    text-align: center;
    line-height: 20pt;
    margin-bottom: 24pt;
  }
  .abstract-box {
    margin-bottom: 18pt;
  }
  .abstract-p {
    text-indent: 2em;
    font-family: KaiTi, STKaiti, serif;
    font-size: 10.5pt;
    line-height: 20pt;
    text-align: justify;
    margin: 0 0 6pt 0;
  }
  .abstract-label {
    font-family: SimHei, sans-serif;
    font-size: 12pt;
    font-weight: bold;
  }
  .keyword-p {
    text-indent: 2em;
    font-family: KaiTi, STKaiti, serif;
    font-size: 10.5pt;
    line-height: 20pt;
    text-align: justify;
    margin: 12pt 0 24pt 0;
  }
  .keyword-label {
    font-family: SimHei, sans-serif;
    font-size: 12pt;
    font-weight: bold;
  }
  h1 {
    font-family: SimHei, sans-serif;
    font-size: 14pt;
    font-weight: bold;
    margin-top: 18pt;
    margin-bottom: 6pt;
    line-height: 20pt;
    page-break-after: avoid;
  }
  h2 {
    font-family: SimHei, sans-serif;
    font-size: 12pt;
    font-weight: bold;
    margin-top: 12pt;
    margin-bottom: 6pt;
    line-height: 20pt;
    page-break-after: avoid;
  }
  h3 {
    font-family: SimHei, sans-serif;
    font-size: 12pt;
    font-weight: bold;
    margin-top: 12pt;
    margin-bottom: 6pt;
    line-height: 20pt;
    page-break-after: avoid;
  }
  h4 {
    font-family: SimHei, sans-serif;
    font-size: 10.5pt;
    font-weight: bold;
    margin-top: 6pt;
    margin-bottom: 3pt;
    line-height: 20pt;
    page-break-after: avoid;
  }
  p {
    text-indent: 2em;
    font-family: 'Times New Roman', SimSun, serif;
    font-size: 10.5pt;
    line-height: 20pt;
    text-align: justify;
    margin: 0 0 6pt 0;
  }
  .caption-p {
    text-indent: 0;
    font-family: SimHei, sans-serif;
    font-size: 10.5pt;
    font-weight: bold;
    text-align: center;
    margin: 12pt 0 6pt 0;
    line-height: 20pt;
  }
  .ref-title {
    font-family: SimHei, sans-serif;
    font-size: 14pt;
    font-weight: bold;
    text-align: center;
    margin-top: 24pt;
    margin-bottom: 12pt;
    line-height: 20pt;
    page-break-after: avoid;
  }
  .ref-p {
    font-family: SimSun, serif;
    font-size: 10.5pt;
    line-height: 20pt;
    padding-left: 2em;
    text-indent: -2em;
    margin: 0 0 6pt 0;
    text-align: justify;
  }
  .en-title {
    font-family: 'Times New Roman', serif;
    font-size: 16pt;
    font-weight: bold;
    text-align: center;
    margin-top: 36pt;
    margin-bottom: 12pt;
    line-height: 24pt;
  }
  .en-abstract-p {
    text-indent: 2em;
    font-family: 'Times New Roman', serif;
    font-size: 12pt;
    line-height: 20pt;
    text-align: justify;
    margin: 0 0 6pt 0;
  }
  .en-keyword-p {
    text-indent: 2em;
    font-family: 'Times New Roman', serif;
    font-size: 12pt;
    line-height: 20pt;
    text-align: justify;
    margin: 12pt 0 12pt 0;
  }
</style>
</head>
<body>
<div class="container">
""")

    # We will process line by line
    i = 0
    in_references = False
    in_english = False
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
            
        # Detect paper title (first non-empty line)
        if i == 0 or (i < 5 and "设计与实现" in line):
            # Replace + with 与 to be perfect
            title_text = line.replace("+", "与")
            html_lines.append(f'  <h1 class="title">{title_text}</h1>')
            i += 1
            continue
            
        # Detect authors/class line
        if "专业班级" in line or "22计科" in line:
            html_lines.append(f'  <div class="authors">{line}</div>')
            i += 1
            continue
            
        # Detect Chinese Abstract
        if line.startswith("摘要：") or line.startswith("　　摘要："):
            abstract_text = line.replace("摘要：", "").replace("　　摘要：", "").strip()
            html_lines.append(f'  <p class="abstract-p"><span class="abstract-label">摘要：</span>{abstract_text}</p>')
            i += 1
            continue
            
        # Detect Chinese Keywords
        if line.startswith("关键词：") or line.startswith("　　关键词："):
            kw_text = line.replace("关键词：", "").replace("　　关键词：", "").strip()
            html_lines.append(f'  <p class="keyword-p"><span class="keyword-label">关键词：</span>{kw_text}</p>')
            i += 1
            continue
            
        # Detect References Section
        if "参  考  文  献" in line or line == "参考文献":
            html_lines.append('  <h1 class="ref-title">参  考  文  献</h1>')
            in_references = True
            i += 1
            continue
            
        # Detect English Title (first line of English abstract block)
        if in_references and ("Design and Implementation" in line or line == "Design and Implementation of a"):
            in_references = False
            in_english = True
            # Read next 2 lines to build full English title if they are separate
            full_en_title = line
            next_idx = i + 1
            while next_idx < len(lines) and lines[next_idx].strip() and not lines[next_idx].strip().startswith("Abstract:"):
                full_en_title += " " + lines[next_idx].strip()
                next_idx += 1
            i = next_idx
            html_lines.append(f'  <h1 class="en-title">{full_en_title}</h1>')
            continue
            
        # Detect English Abstract
        if in_english and line.startswith("Abstract:"):
            en_abs_text = line.replace("Abstract:", "").strip()
            html_lines.append(f'  <p class="en-abstract-p"><strong style="font-size: 12pt;">Abstract:</strong> {en_abs_text}</p>')
            i += 1
            continue
            
        # Detect English Key Words
        if in_english and line.startswith("Keywords:"):
            en_kw_text = line.replace("Keywords:", "").strip()
            html_lines.append(f'  <p class="en-keyword-p"><strong style="font-size: 12pt;">Keywords:</strong> {en_kw_text}</p>')
            i += 1
            continue
            
        # Parse References Items
        if in_references:
            # Lines are of format [1] Cao Y...
            ref_match = re.match(r'^\[(\d+)\]\s*(.*)', line)
            if ref_match:
                ref_num = ref_match.group(1)
                ref_content = ref_match.group(2).strip()
                # Check if next lines are part of the reference (not starting with [ or title)
                next_idx = i + 1
                while next_idx < len(lines) and lines[next_idx].strip() and not re.match(r'^\[\d+\]', lines[next_idx].strip()) and "Design and Implementation" not in lines[next_idx]:
                    ref_content += " " + lines[next_idx].strip()
                    next_idx += 1
                i = next_idx
                html_lines.append(f'  <p class="ref-p">[{ref_num}]&nbsp;&nbsp;{ref_content}</p>')
                continue
                
        # Parse standard headings or paragraphs
        heading_match = re.match(r'^(\d+(\.\d+)*)\s+(.*)', line)
        if heading_match and not in_english:
            num = heading_match.group(1)
            level = len(num.split('.'))
            text = heading_match.group(3).strip()
            
            if level == 1:
                html_lines.append(f'  <h1>{num}  {text}</h1>')
            elif level == 2:
                html_lines.append(f'  <h2>{num}  {text}</h2>')
            elif level == 3:
                html_lines.append(f'  <h3>{num}  {text}</h3>')
            else:
                html_lines.append(f'  <h4>{num}  {text}</h4>')
            i += 1
            continue
            
        # Detect Table Caption
        table_caption_match = re.match(r'^表(\d+)\s+(.*)', line)
        if table_caption_match:
            t_num = int(table_caption_match.group(1))
            t_text = table_caption_match.group(2).strip()
            html_lines.append(f'  <p class="caption-p">表{t_num}  {t_text}</p>')
            
            # Embed Table
            t_key = f"table_{t_num - 1}"
            if t_key in tables_dict:
                t_rows = tables_dict[t_key]
                if t_num <= 4:
                    html_lines.append(render_db_table(t_rows))
                else:
                    html_lines.append(render_test_table(t_rows, t_num))
            i += 1
            continue
            
        # Detect Figure Caption
        fig_caption_match = re.match(r'^图(\d+)\s+(.*)', line)
        if fig_caption_match:
            f_num = int(fig_caption_match.group(1))
            f_text = fig_caption_match.group(2).strip()
            html_lines.append(f'  <p class="caption-p">图{f_num}  {f_text}</p>')
            i += 1
            continue
            
        # Default standard paragraph
        # Clean double byte spaces at start
        p_text = line.lstrip('　').lstrip()
        html_lines.append(f'  <p>{p_text}</p>')
        i += 1

    html_lines.append("""</div>
</body>
</html>
""")

    # Write HTML file
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    with open(path_html, "w", encoding="utf-8") as out:
        out.write("\n".join(html_lines))
        
    print(f"Successfully generated HTML manuscript at {path_html}")

if __name__ == "__main__":
    main()
