font_c_path = r'd:\project_stm32\1.homework\demo6_oled_连续混合文字\font\FontDotMatrix16.c'

with open(font_c_path, 'rb') as f:
    c_content = f.read()

target = b'"\xb6\xc8",\r\n};'
replacement = b'"\xb6\xc8", "\xc0\xee", "\xc1\xeb", "\xd5\xdc",\r\n};'

if target in c_content:
    c_content = c_content.replace(target, replacement)
    print('Index array successfully updated!')
else:
    print('Target not found!')

with open(font_c_path, 'wb') as f:
    f.write(c_content)
