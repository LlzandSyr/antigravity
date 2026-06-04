import os

def find_function_lines(filepath, func_name):
    if not os.path.exists(filepath):
        return f"File {os.path.basename(filepath)} not found"
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        
        matches = []
        for i, line in enumerate(lines):
            if func_name in line and ("(" in line or "::" in line) and not line.strip().startswith("//") and not line.strip().endswith(";"):
                matches.append((i + 1, line.strip()))
        return matches
    except Exception as e:
        return f"Error: {str(e)}"

p1_c = r"c:\Users\86135\Desktop\面试题\阶段项目1\流光文件FluxFile+李怜哲\lv_port_linux_frame_buffer-release-v8.2\dir_file_list\dir_file_list.c"
funcs = ["Dir_Search_Show", "Check_Valid_Pic", "Show_Pic", "pic_win_timer_cb", "Update_Dir_List", "spinner_timer_cb", "Show_Dirfile_Windows", "Exit_Pro", "Destroy_List", "Page_Btn_Event", "Close_Pic_Win"]

print("=== Phase 1 Verification ===")
print(f"File: dir_file_list.c (size: {os.path.getsize(p1_c)})")
for f in funcs:
    print(f"  {f}: {find_function_lines(p1_c, f)}")
