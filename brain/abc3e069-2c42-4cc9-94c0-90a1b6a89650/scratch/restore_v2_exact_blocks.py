import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    path_v2 = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v2.txt"
    
    with open(path_v2, "r", encoding="utf-8") as f:
        v2_content = f.read()
        
    with open(path_txt, "r", encoding="utf-8") as f:
        v4_content = f.read()

    # We want to extract Chapter 4.3 Database design from v2
    # In v2:
    # "4.3  数据库设计" to right before "5  系统实现"
    v2_ch4_start = v2_content.find("4.3  数据库设计")
    v2_ch5_start = v2_content.find("5  系统实现")
    
    if v2_ch4_start != -1 and v2_ch5_start != -1:
        v2_ch4_block = v2_content[v2_ch4_start:v2_ch5_start]
        print("Successfully extracted Chapter 4.3 from v2")
    else:
        print("Error: Could not extract Ch4.3 from v2")
        return
        
    # We want to extract Chapter 5 from v2
    # In v2:
    # "5  系统实现" to right before "6  系统测试"
    v2_ch6_start = v2_content.find("6  系统测试")
    if v2_ch5_start != -1 and v2_ch6_start != -1:
        v2_ch5_block = v2_content[v2_ch5_start:v2_ch6_start]
        print("Successfully extracted Chapter 5 from v2")
    else:
        print("Error: Could not extract Chapter 5 from v2")
        return

    # We want to extract Chapter 6.1 to 6.3 (Test case tables) from v2
    # In v2:
    # "6  系统测试" to right before "6.4  测试结论"
    v2_ch6_conclusion = v2_content.find("6.4  测试结论")
    if v2_ch6_start != -1 and v2_ch6_conclusion != -1:
        v2_ch6_block = v2_content[v2_ch6_start:v2_ch6_conclusion]
        print("Successfully extracted Chapter 6 tables from v2")
    else:
        print("Error: Could not extract Chapter 6 tables from v2")
        return

    # Now let's do the replacements in v4_content
    # 1. Replace 4.3 in v4
    v4_ch4_start = v4_content.find("4.3  数据库设计")
    v4_ch5_start = v4_content.find("5  系统实现")
    
    if v4_ch4_start != -1 and v4_ch5_start != -1:
        v4_content = v4_content[:v4_ch4_start] + v2_ch4_block + v4_content[v4_ch5_start:]
        print("Replaced Ch4.3 in v4")
    else:
        print("Error: Could not find Ch4.3 in v4")
        return
        
    # After 4.3 is replaced, the index of "5  系统实现" and "6  系统测试" in updated v4_content might shift, so we find them again
    v4_ch5_start = v4_content.find("5  系统实现")
    v4_ch6_start = v4_content.find("6  系统测试")
    
    if v4_ch5_start != -1 and v4_ch6_start != -1:
        v4_content = v4_content[:v4_ch5_start] + v2_ch5_block + v4_content[v4_ch6_start:]
        print("Replaced Chapter 5 in v4")
    else:
        print("Error: Could not find Chapter 5 in v4")
        return
        
    # Find Chapter 6 and its conclusion in updated v4_content
    v4_ch6_start = v4_content.find("6  系统测试")
    v4_ch6_conclusion = v4_content.find("6.4  测试结论")
    
    if v4_ch6_start != -1 and v4_ch6_conclusion != -1:
        v4_content = v4_content[:v4_ch6_start] + v2_ch6_block + v4_content[v4_ch6_conclusion:]
        print("Replaced Chapter 6 tables in v4")
    else:
        print("Error: Could not find Chapter 6 tables in v4")
        return
        
    with open(path_txt, "w", encoding="utf-8") as f:
        f.write(v4_content)
        
    print("Successfully restored Chapter 4.3, Chapter 5 and Chapter 6 tables in v4!")

if __name__ == "__main__":
    main()
