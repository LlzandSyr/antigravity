import re
import os

p2_c_path = r"c:\Users\86135\Desktop\面试题\阶段项目2\李怜哲+流光云盘FluxCloud\lv_port_linux_frame_buffer-release-v8.2\dir_file_list\dir_file_list.c"

def get_function_range(filepath, func_signature_substring):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    
    start_line = None
    for idx, line in enumerate(lines):
        if func_signature_substring in line and ("(" in line or "::" in line) and not line.strip().startswith("//") and not line.strip().endswith(";"):
            start_line = idx + 1
            break
            
    if start_line is None:
        return None
        
    # Find the closing brace of the function
    # We count open and close braces starting from the start line
    brace_count = 0
    found_brace = False
    end_line = None
    
    for idx in range(start_line - 1, len(lines)):
        line = lines[idx]
        # Ignore comments or string contents when counting braces is hard, but simple counting works for well-formatted C code
        for char in line:
            if char == '{':
                brace_count += 1
                found_brace = True
            elif char == '}':
                brace_count -= 1
                
        if found_brace and brace_count == 0:
            end_line = idx + 1
            break
            
    return start_line, end_line

p2_funcs = [
    ("Show_Dirfile_Windows", "P_DBI Show_Dirfile_Windows()"),
    ("spinner_timer_cb", "void spinner_timer_cb("),
    ("Update_Dir_List", "void Update_Dir_List("),
    ("Dir_Search_Show", "int Dir_Search_Show("),
    ("Destroy_List", "int    Destroy_List("),
    ("Check_Valid_Pic", "int  Check_Valid_Pic("),
    ("pic_win_timer_cb", "void pic_win_timer_cb("),
    ("Show_Pic", "void Show_Pic("),
    ("Page_Btn_Event", "static void Page_Btn_Event("),
    ("Close_Pic_Win", "void Close_Pic_Win("),
    ("Exit_Pro", "void Exit_Pro("),
    ("Get_Weather_Thread", "void * Get_Weather_Thread("),
    ("Load_Cloud_File_List", "void Load_Cloud_File_List("),
    ("upload_thread", "void * upload_thread("),
    ("download_thread", "void * download_thread("),
    ("transfer_timer_cb", "static void transfer_timer_cb("),
]

print("=== Phase 2 dir_file_list.c Function Ranges ===")
for name, sig in p2_funcs:
    res = get_function_range(p2_c_path, sig)
    if res:
        print(f"{name}: {res[0]}~{res[1]}")
    else:
        # Fallback to search by name
        res = get_function_range(p2_c_path, name)
        if res:
            print(f"{name} (fallback): {res[0]}~{res[1]}")
        else:
            print(f"{name}: Not found")
