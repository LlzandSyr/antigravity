# Convert main.c from UTF-8 to GBK
try:
    with open(r'd:\project_stm32\1.homework\demo1_spi_lcd_移植\main.c', 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(r'd:\project_stm32\1.homework\demo1_spi_lcd_移植\main.c', 'w', encoding='gbk', errors='replace') as f:
        f.write(content)
    print("Successfully converted main.c to GBK encoding.")
except Exception as e:
    print(f"Error during conversion: {e}")
