import re

path = r'd:\project_stm32\1.homework\demo6_oled_连续混合文字\font\FontDotMatrix16.c'
content = open(path, 'r', encoding='gbk', errors='ignore').read()

idx_block = re.search(r'g_font_dot_matrix_16_index\[(.*?)\]\s*=\s*\{(.*?)\};', content, re.DOTALL)
if idx_block:
    size_decl = idx_block.group(1).strip()
    elements = re.findall(r'\"(.*?)\"', idx_block.group(2))
    print('Index size declared in brackets:', size_decl)
    print('Index elements count:', len(elements))
    print('Last 10 elements in Index:', elements[-10:])
else:
    print('No index block found')

data_block = re.search(r'g_font_dot_matrix_16\[(.*?)\]\[32\]\s*=\s*\{(.*?)\};', content, re.DOTALL)
if data_block:
    size_decl = data_block.group(1).strip()
    brackets = re.findall(r'\{([^{}]*)\}', data_block.group(2))
    print('Data size declared in brackets:', size_decl)
    print('Data elements count:', len(brackets))
else:
    print('No data block found')
