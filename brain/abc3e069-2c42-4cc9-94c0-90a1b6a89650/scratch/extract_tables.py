import re

def main():
    # Read the thesis file
    path_thesis = r"C:\Users\86135\Desktop\优秀毕业论文\大论文原文.md"
    try:
        with open(path_thesis, "r", encoding="gb18030") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading gb18030: {e}")
        try:
            with open(path_thesis, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e2:
            print(f"Error reading utf-8: {e2}")
            return

    # Find markdown tables
    # Markdown tables are lines starting with | and containing | 
    lines = content.split('\n')
    tables = {}
    current_table = []
    current_title = ""
    
    for i, line in enumerate(lines):
        # Look for table captions
        caption_match = re.search(r'(表\d+[\s\w（）\(\)]+)', line)
        if caption_match:
            current_title = caption_match.group(1).strip()
            print(f"Found caption candidate at line {i}: {current_title}")
            
        if line.strip().startswith('|'):
            current_table.append(line.strip())
        elif current_table:
            # We finished a table block
            if current_title:
                tables[current_title] = current_table
            else:
                tables[f"table_{len(tables)}"] = current_table
            current_table = []
            current_title = ""

    # Let's save the extracted tables
    with open("extracted_tables.txt", "w", encoding="utf-8") as out:
        for title, rows in tables.items():
            out.write(f"=== {title} ===\n")
            for row in rows:
                out.write(row + "\n")
            out.write("\n")
            
    print(f"Extracted {len(tables)} tables and saved to extracted_tables.txt")

if __name__ == "__main__":
    main()
