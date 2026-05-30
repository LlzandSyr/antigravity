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
    html = ['<center>', '  <table align="center" style="border-collapse: collapse; border: 1px solid black; width: 90%; max-width: 650px; margin: 6pt auto 12pt auto; font-size: 10.5pt; font-family: SimSun, serif;">']
    headers = [col.strip() for col in rows[0].split('|')[1:-1]]
    html.append('    <tr style="font-weight: bold; background-color: #f2f2f2; text-align: center;">')
    for h in headers:
        html.append(f'      <th style="border: 1px solid black; padding: 5pt 8pt; text-align: center;">{h}</th>')
    html.append('    </tr>')
    for r in rows[2:]:
        cols = [col.strip() for col in r.split('|')[1:-1]]
        html.append('    <tr>')
        for c in cols:
            html.append(f'      <td style="border: 1px solid black; padding: 5pt 8pt; text-align: center;">{c}</td>')
        html.append('    </tr>')
    html.append('  </table>')
    html.append('</center>')
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
            
    html = ['<center>', '  <table align="center" style="border-collapse: collapse; border: 1px solid black; width: 90%; max-width: 650px; margin: 6pt auto 12pt auto; font-size: 10.5pt; font-family: SimSun, serif;">']
    html.append(f'    <tr>')
    html.append(f'      <td colspan="5" style="border: 1px solid black; padding: 5pt 8pt; font-weight: bold; background-color: #f2f2f2;">用例编号：{case_num} &nbsp;&nbsp;&nbsp;&nbsp; 测试场景：{test_scene} &nbsp;&nbsp;&nbsp;&nbsp; 测试对象：{test_target}</td>')
    html.append(f'    </tr>')
    
    grid_header_idx = -1
    for idx, r in enumerate(rows):
        if "序号" in r:
            grid_header_idx = idx
            break
            
    if grid_header_idx != -1:
        headers = [col.strip() for col in rows[grid_header_idx].split('|')[1:-1]]
        html.append('    <tr style="font-weight: bold; background-color: #f9f9f9; text-align: center;">')
        widths = ["8%", "25%", "37%", "22%", "8%"]
        for i, h in enumerate(headers):
            html.append(f'      <th style="border: 1px solid black; padding: 5pt 8pt; width: {widths[i]}; text-align: center;">{h}</th>')
        html.append('    </tr>')
        for r in rows[grid_header_idx+1:]:
            cols = [col.strip() for col in r.split('|')[1:-1]]
            html.append('    <tr>')
            for i, c in enumerate(cols):
                align = "left"
                if i == 0 or i == 4:
                    align = "center"
                html.append(f'      <td style="border: 1px solid black; padding: 5pt 8pt; text-align: {align};">{c}</td>')
            html.append('    </tr>')
    html.append('  </table>')
    html.append('</center>')
    return "\n".join(html)

def main():
    scratch_dir = r"C:\Users\86135\.gemini\antigravity\brain\abc3e069-2c42-4cc9-94c0-90a1b6a89650\scratch"
    tables_dict = parse_extracted_tables(scratch_dir)
    
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.split('\n')
    
    # State-based paragraph grouping
    blocks = []
    current_block = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("|"):
            if current_block:
                blocks.append(current_block)
                current_block = []
            continue
            
        is_new_block = False
        
        if re.match(r'^\d+(\.\d+)*\s+', stripped):
            is_new_block = True
        elif stripped.startswith("摘要：") or stripped.startswith("　　摘要：") or stripped.startswith("关键词：") or stripped.startswith("　　关键词："):
            is_new_block = True
        elif re.match(r'^(图|表)\d+\s+', stripped):
            is_new_block = True
        elif "参  考  文  献" in stripped or stripped == "参考文献":
            is_new_block = True
        elif re.match(r'^\[\d+\]', stripped):
            is_new_block = True
        elif stripped.startswith("Abstract:") or stripped.startswith("Keywords:") or "Design and Implementation" in stripped:
            is_new_block = True
        elif line.startswith("　　"):
            is_new_block = True
        elif "专业班级" in stripped or "22计科" in stripped:
            is_new_block = True
            
        if is_new_block:
            if current_block:
                blocks.append(current_block)
            current_block = [line]
        else:
            if current_block:
                current_block.append(line)
            else:
                current_block = [line]
                
    if current_block:
        blocks.append(current_block)
        
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

    in_references = False
    in_english = False
    
    for block in blocks:
        # Determine join style
        # English block lines are joined with a space
        block_text_first = block[0].strip()
        
        is_block_english = in_english or block_text_first.startswith("Abstract:") or block_text_first.startswith("Keywords:") or "Design and Implementation" in block_text_first
        
        # We also treat the references after the English Abstract begins as English
        if in_english:
            is_block_english = True
            
        if is_block_english:
            joined_content = " ".join([l.strip() for l in block])
        else:
            joined_content = "".join([l.strip() for l in block])
            
        # Detect special headers
        if "参  考  文  献" in joined_content or joined_content == "参考文献":
            html_lines.append('  <h1 class="ref-title">参  考  文  献</h1>')
            in_references = True
            continue
            
        # English Title
        if in_references and ("Design and Implementation" in joined_content):
            in_references = False
            in_english = True
            html_lines.append(f'  <h1 class="en-title">{joined_content}</h1>')
            continue
            
        # English Abstract
        if in_english and joined_content.startswith("Abstract:"):
            en_abs_text = joined_content.replace("Abstract:", "").strip()
            html_lines.append(f'  <p class="en-abstract-p"><strong style="font-size: 12pt;">Abstract:</strong> {en_abs_text}</p>')
            continue
            
        # English Keywords
        if in_english and joined_content.startswith("Keywords:"):
            en_kw_text = joined_content.replace("Keywords:", "").strip()
            html_lines.append(f'  <p class="en-keyword-p"><strong style="font-size: 12pt;">Keywords:</strong> {en_kw_text}</p>')
            continue
            
        # Paper Title (starts the doc)
        if len(html_lines) <= 20 and ("多模态AI图库系统" in joined_content and "设计与实现" in joined_content):
            title_text = joined_content.replace("+", "与")
            html_lines.append(f'  <h1 class="title">{title_text}</h1>')
            continue
            
        # Class / Authors
        if "专业班级" in joined_content or "22计科" in joined_content:
            html_lines.append(f'  <div class="authors">{joined_content}</div>')
            continue
            
        # Chinese Abstract
        if joined_content.startswith("摘要：") or joined_content.startswith("　　摘要："):
            abstract_text = joined_content.replace("摘要：", "").replace("　　摘要：", "").strip()
            html_lines.append(f'  <p class="abstract-p"><span class="abstract-label">摘要：</span>{abstract_text}</p>')
            continue
            
        # Chinese Keywords
        if joined_content.startswith("关键词：") or joined_content.startswith("　　关键词："):
            kw_text = joined_content.replace("关键词：", "").replace("　　关键词：", "").strip()
            html_lines.append(f'  <p class="keyword-p"><span class="keyword-label">关键词：</span>{kw_text}</p>')
            continue
            
        # Reference items
        if in_references:
            ref_match = re.match(r'^\[(\d+)\]\s*(.*)', joined_content)
            if ref_match:
                ref_num = ref_match.group(1)
                ref_content = ref_match.group(2).strip()
                html_lines.append(f'  <p class="ref-p">[{ref_num}]&nbsp;&nbsp;{ref_content}</p>')
                continue
                
        # Headings
        heading_match = re.match(r'^(\d+(\.\d+)*)\s+(.*)', joined_content)
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
            continue
            
        # Table Caption
        table_caption_match = re.match(r'^表(\d+)\s+(.*)', joined_content)
        if table_caption_match:
            t_num = int(table_caption_match.group(1))
            t_text = table_caption_match.group(2).strip()
            # Table caption ABOVE the table, centered
            html_lines.append(f'  <p style="text-indent: 0; font-family: SimHei, sans-serif; font-size: 10.5pt; font-weight: bold; text-align: center; margin: 12pt 0 6pt 0; line-height: 20pt;">表{t_num}  {t_text}</p>')
            
            t_key = f"table_{t_num - 1}"
            if t_key in tables_dict:
                t_rows = tables_dict[t_key]
                if t_num <= 4:
                    html_lines.append(render_db_table(t_rows))
                else:
                    html_lines.append(render_test_table(t_rows, t_num))
            continue
            
        # Figure Caption
        fig_caption_match = re.match(r'^图(\d+)\s+(.*)', joined_content)
        if fig_caption_match:
            f_num = int(fig_caption_match.group(1))
            f_text = fig_caption_match.group(2).strip()
            # Figure placeholder box first
            html_lines.append(f'  <div style="text-align: center; margin: 12pt auto 6pt auto; width: 80%; max-width: 550px; border: 1px dashed #777777; padding: 25pt; font-family: SimSun, serif; font-size: 10.5pt; color: #555555; background-color: #fafafa; border-radius: 4px;">【图 {f_num} {f_text} 截图占位符，在此插入图片】</div>')
            # Figure caption BELOW the box, centered
            html_lines.append(f'  <p style="text-indent: 0; font-family: SimHei, sans-serif; font-size: 10.5pt; font-weight: bold; text-align: center; margin: 6pt 0 12pt 0; line-height: 20pt;">图{f_num}  {f_text}</p>')
            continue
            
        # Standard paragraph
        p_text = joined_content.lstrip('　').lstrip()
        html_lines.append(f'  <p>{p_text}</p>')

    html_lines.append("""</div>
</body>
</html>
""")

    # Write HTML file
    path_html = r"C:\Users\86135\Desktop\优秀毕业论文\稿件.html"
    with open(path_html, "w", encoding="utf-8") as out:
        out.write("\n".join(html_lines))
        
    print(f"Successfully generated clean HTML manuscript at {path_html}")

if __name__ == "__main__":
    main()
