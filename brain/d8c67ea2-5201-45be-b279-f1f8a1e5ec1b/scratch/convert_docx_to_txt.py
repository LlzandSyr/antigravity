import docx
import os
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import Table
from docx.text.paragraph import Paragraph

def iter_block_items(parent):
    if isinstance(parent, docx.document.Document):
        parent_elm = parent.element.body
    elif isinstance(parent, docx.table._Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("Unknown parent type")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def format_cell_text(cell):
    lines = []
    for p in cell.paragraphs:
        t = p.text.strip()
        if t:
            lines.append(t)
    # Join paragraphs with newline or space, but escape newlines for markdown tables
    full_text = "\n".join(lines)
    return full_text.replace("\n", " <br> ")

def apply_replacements_str(text, reps):
    for old, new in reps:
        text = text.replace(old, new)
    return text

def convert_docx_to_markdown_txt(docx_path, txt_path, reps):
    if not os.path.exists(docx_path):
        print(f"File {docx_path} not found")
        return
    
    doc = docx.Document(docx_path)
    lines = []
    
    for item in iter_block_items(doc):
        if isinstance(item, Paragraph):
            text = item.text.strip()
            # Detect basic lists or headings by style
            style_name = item.style.name.lower()
            if text:
                if "heading 1" in style_name:
                    lines.append(f"\n# {text}\n")
                elif "heading 2" in style_name:
                    lines.append(f"\n## {text}\n")
                elif "heading 3" in style_name:
                    lines.append(f"\n### {text}\n")
                elif "heading" in style_name:
                    lines.append(f"\n# {text}\n")
                elif "list" in style_name or text.startswith("-") or text.startswith("*"):
                    lines.append(f"- {text.lstrip('-* ')}")
                else:
                    lines.append(text)
            else:
                lines.append("") # empty paragraph
        elif isinstance(item, Table):
            lines.append("") # space before table
            # Check row count and col count
            rows = item.rows
            if len(rows) > 0:
                # Header row
                header_cells = [format_cell_text(c) for c in rows[0].cells]
                lines.append("| " + " | ".join(header_cells) + " |")
                lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
                
                # Data rows
                for r_idx in range(1, len(rows)):
                    cells = [format_cell_text(c) for c in rows[r_idx].cells]
                    lines.append("| " + " | ".join(cells) + " |")
            lines.append("") # space after table

    # Combine to single string
    full_content = "\n".join(lines)
    # Apply versioning and line number corrections
    full_content = apply_replacements_str(full_content, reps)
    
    # Save as .txt
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"Successfully converted and saved: {os.path.basename(txt_path)}")

# Phase 2 V4.0 Replacements
p2_reps = [
    ("FluxCloud 流光云盘（阶段二）", "FluxCloud 流光云盘（阶段四）"),
    ("FluxCloud_V2.0", "FluxCloud_V4.0"),
    ("dir_file_list/dir_file_list.c（1167行）", "dir_file_list/dir_file_list.c（在阶段四最终版本中已扩展至2684行，以下已适配实际行号）"),
    ("第489~693行", "第916~1128行"),
    ("第787~803行", "第1222~1238行"),
    ("第941~960行", "第1376~1395行"),
    ("第809~935行", "第1244~1370行"),
    ("第453~482行", "第880~909行"),
    ("第403~447行", "第830~874行"),
    ("第199~384行", "第564~811行"),
    ("第1124~1166行", "第1559~1603行"),
    ("第741~781行", "第1176~1216行"),
    ("第968~1087行", "第1403~1522行"),
    ("第1093~1107行", "第1528~1542行"),
    ("第2551行", "第2557行"),
    ("第2568-2578行", "第2564~2586行"),
    ("第2609行", "第2614行"),
    ("第2638-2670行", "第2639~2670行")
]

# Phase 3 V4.0 Replacements
p3_reps = [
    ("Aura_V2.0", "Aura_V4.0"),
    ("changeQty(): menudelegate.cpp 第209~220行", "changeQty(): menumodel.cpp 第77~90行"),
    ("loadFromJson(): 第45~70行", "loadFromJson(): 第49~68行"),
    ("OrderPage::initUI(): Aura_Client/clientwindow.cpp 第364~386行", "OrderPage::initUI(): Aura_Client/clientwindow.cpp 第339~412行"),
]

p2_docx = r"c:\Users\86135\Desktop\面试题\阶段项目2\FluxCloud_V2.0_项目功能逐条复盘（含AI扩展）.docx"
p3_docx = r"c:\Users\86135\Desktop\面试题\阶段项目3\Aura_V2.0_项目功能逐条复盘（含AI扩展）.docx"

p2_txt_v4 = r"c:\Users\86135\Desktop\面试题\阶段项目2\FluxCloud_V4.0_项目功能逐条复盘（含AI扩展）.txt"
p3_txt_v4 = r"c:\Users\86135\Desktop\面试题\阶段项目3\Aura_V4.0_项目功能逐条复盘（含AI扩展）.txt"

convert_docx_to_markdown_txt(p2_docx, p2_txt_v4, p2_reps)
convert_docx_to_markdown_txt(p3_docx, p3_txt_v4, p3_reps)
print("Conversion completed successfully!")
