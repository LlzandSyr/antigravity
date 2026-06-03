import os

font_path = r'd:\project_stm32\1.homework\demo3_oled_汉字\hardware\oled\oledfont.h'
main_path = r'd:\project_stm32\1.homework\demo3_oled_汉字\main.c'

# 1. Modify oledfont.h
with open(font_path, 'rb') as f:
    content_bytes = f.read()

target = b'}\r\n\r\n};'
replacement = b''',

/* "Li", 6 */
{
  0x80, 0x84, 0x44, 0x44, 0x24, 0x14, 0x0C, 0xFF, 0x0C, 0x14, 0x24, 0x44, 0x44, 0x84, 0x80, 0x00, 
  0x08, 0x08, 0x08, 0x08, 0x09, 0x49, 0x89, 0x79, 0x0D, 0x0B, 0x09, 0x08, 0x08, 0x08, 0x08, 0x00, 
},
/* "Lian", 7 */
{
  0x80, 0x70, 0x00, 0xFF, 0x08, 0x50, 0x20, 0x10, 0x0C, 0x23, 0xCC, 0x10, 0x20, 0x40, 0x40, 0x00, 
  0x00, 0x00, 0x00, 0xFF, 0x00, 0x00, 0x01, 0x09, 0x11, 0x21, 0xD1, 0x0D, 0x03, 0x00, 0x00, 0x00, 
},
/* "Zhe", 8 */
{
  0x00, 0x24, 0xA4, 0x24, 0xFF, 0x14, 0x14, 0x80, 0x7E, 0x12, 0x12, 0x12, 0xF1, 0x11, 0x10, 0x00, 
  0x00, 0x00, 0x00, 0xFD, 0x44, 0x44, 0x45, 0x44, 0x44, 0x44, 0x44, 0xFC, 0x01, 0x00, 0x00, 0x00, 
}
};'''

if target in content_bytes:
    new_bytes = content_bytes.replace(target, replacement)
    with open(font_path, 'wb') as f:
        f.write(new_bytes)
    print('Modified oledfont.h successfully!')
else:
    print('Error: Target not found in oledfont.h')

# 2. Modify main.c
with open(main_path, 'rb') as f:
    main_bytes = f.read()

main_replacement = b'OLED_ShowCHinese(0,0,6); // Li\r\n\tOLED_ShowCHinese(18,0,7); // Lian\r\n\tOLED_ShowCHinese(36,0,8); // Zhe'

import re
# Find OLED_ShowCHinese(0,0,139); followed by optional comments, whitespace, and the other two calls
pattern = rb'OLED_ShowCHinese\(\s*0\s*,\s*0\s*,\s*139\s*\);[^\r\n]*\r?\n\s*OLED_ShowCHinese\(\s*18\s*,\s*0\s*,\s*140\s*\);[^\r\n]*\r?\n\s*OLED_ShowCHinese\(\s*36\s*,\s*0\s*,\s*141\s*\);'
match = re.search(pattern, main_bytes)
if match:
    new_main = main_bytes[:match.start()] + main_replacement + main_bytes[match.end():]
    with open(main_path, 'wb') as f:
        f.write(new_main)
    print('Modified main.c using pattern matching successfully!')
else:
    print('Error: Target call pattern not found in main.c')
