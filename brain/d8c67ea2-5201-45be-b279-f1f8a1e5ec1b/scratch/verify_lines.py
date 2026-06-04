import os

# Helper to find function start/end line in a file
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

# We can also print specific line segments
def get_file_lines(filepath, start, end):
    if not os.path.exists(filepath):
        return "File not found"
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        return "".join(lines[start-1:end])
    except Exception as e:
        return str(e)

# Phase 3 files
p3_base = r"c:\Users\86135\Desktop\面试题\阶段项目3\李怜哲+微光智控餐饮终端"
p3_files = {
    "serverwindow.cpp": os.path.join(p3_base, "Aura_Server", "serverwindow.cpp"),
    "clientwindow.cpp": os.path.join(p3_base, "Aura_Client", "clientwindow.cpp"),
    "menumodel.cpp": os.path.join(p3_base, "Aura_Client", "menumodel.cpp"),
    "menudelegate.cpp": os.path.join(p3_base, "Aura_Client", "menudelegate.cpp"),
    "weatherfetcher.cpp": os.path.join(p3_base, "Aura_Client", "weatherfetcher.cpp"),
}

# Phase 2 files
p2_base = r"c:\Users\86135\Desktop\面试题\阶段项目2\李怜哲+流光云盘FluxCloud\lv_port_linux_frame_buffer-release-v8.2"
p2_files = {
    "dir_file_list.c": os.path.join(p2_base, "dir_file_list", "dir_file_list.c"),
    "server.c": os.path.join(p2_base, "dir_file_list", "server", "server.c"),
    "threadpool.c": os.path.join(p2_base, "dir_file_list", "server", "threadpool.c"),
}

print("=== Phase 3 Verification ===")
for name, path in p3_files.items():
    print(f"File: {name} (size: {os.path.getsize(path) if os.path.exists(path) else 'N/A'})")
    if name == "serverwindow.cpp":
        funcs = ["initNetwork", "onNewConnection", "onSocketReadyRead", "handleMessage", "initDatabase", "sendMenuTo", "handleOrderSubmit"]
    elif name == "clientwindow.cpp":
        funcs = ["initNetwork", "onConnected", "requestMenu", "onReadyRead", "handleMessage", "onModelQtyChanged", "submitOrder", "CartDialog::initUI"]
    elif name == "menumodel.cpp":
        funcs = ["rowCount", "data", "setQty", "loadFromJson"]
    elif name == "menudelegate.cpp":
        funcs = ["paint", "editorEvent", "plusBtnRect", "minusBtnRect", "qtyTextRect", "changeQty"]
    elif name == "weatherfetcher.cpp":
        funcs = ["fetchOnce", "onReplyFinished"]
    else:
        funcs = []
    for f in funcs:
        print(f"  {f}: {find_function_lines(path, f)}")

print("\n=== Phase 2 Verification ===")
for name, path in p2_files.items():
    print(f"File: {name} (size: {os.path.getsize(path) if os.path.exists(path) else 'N/A'})")
    if name == "dir_file_list.c":
        funcs = ["Dir_Search_Show", "Check_Valid_Pic", "Show_Pic", "pic_win_timer_cb", "Update_Dir_List", "spinner_timer_cb", "Show_Dirfile_Windows", "Exit_Pro", "Destroy_List", "Page_Btn_Event", "Close_Pic_Win", "Get_Weather_Thread", "Load_Cloud_File_List", "upload_thread", "download_thread", "transfer_timer_cb"]
    elif name == "server.c":
        funcs = ["handle_upload", "handle_download", "handle_list", "add_client", "remove_client", "show_clients", "client_service", "handle_register", "handle_login"]
    elif name == "threadpool.c":
        funcs = ["threadpool_init", "thread_routine", "threadpool_add_task", "threadpool_destroy"]
    else:
        funcs = []
    for f in funcs:
        print(f"  {f}: {find_function_lines(path, f)}")
