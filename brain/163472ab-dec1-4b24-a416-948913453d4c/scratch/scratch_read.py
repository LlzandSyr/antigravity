with open(r'd:\project_stm32\1.homework\demo1_spi_lcd_移植\main.c', 'rb') as f:
    content = f.read()

start = content.find(b'g_font_dot_matrix_32[142][128]')
if start != -1:
    # Let's find the inner blocks
    inner_blocks = []
    in_block = False
    current_block = bytearray()
    start_inner = content.find(b'{', start) + 1
    
    for char_idx in range(start_inner, len(content)):
        c = content[char_idx:char_idx+1]
        if c == b'{':
            in_block = True
            current_block = bytearray()
        elif c == b'}':
            if in_block:
                inner_blocks.append(current_block)
                in_block = False
        else:
            if in_block:
                current_block.extend(c)
        if len(inner_blocks) >= 142:
            break
            
    print(f"Total inner blocks found: {len(inner_blocks)}")
    for idx in [139, 140, 141]:
        if idx < len(inner_blocks):
            block = inner_blocks[idx]
            # Split by comma and count non-empty
            bytes_list = [x.strip() for x in block.split(b',') if x.strip()]
            print(f"Index {idx}: defined with {len(bytes_list)} bytes.")
            print(f"First 10 bytes: {bytes_list[:10]}")
        else:
            print(f"Index {idx} is out of range!")
else:
    print("g_font_dot_matrix_32 not found")
