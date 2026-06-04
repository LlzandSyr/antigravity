import os

p2_txt_path = r"c:\Users\86135\Desktop\面试题\阶段项目2\FluxCloud_V4.0_项目功能逐条复盘（含AI扩展）.txt"
p3_txt_path = r"c:\Users\86135\Desktop\面试题\阶段项目3\Aura_V4.0_项目功能逐条复盘（含AI扩展）.txt"

# ----------------- FluxCloud V4.0 Content -----------------
p2_content = """# =========================================================================
#  FluxCloud V4.0 - 项目功能逐条复盘（含AI扩展与官方核对表适配）
#  第一期：FluxFile 流光文件浏览器（即阶段项目一）
#  第二期：FluxCloud 流光云盘（即阶段项目二）
# =========================================================================

此文档根据官方下发的《项目进度功能核对表》逐条整理，全面核对并复盘了具体代码的实现细节、源码文件位置、以及具体行号，便于面试前查阅与快速回顾。

=========================================================================
第一期：FluxFile 流光文件浏览器（阶段一核心功能）
=========================================================================

-------------------------------------------------------------------------
【难度等级一 (60~80分)】
-------------------------------------------------------------------------
[✓] 1. 使用目录检索，检索指定的目录中的图片（图库图片），点击图片图标打开新窗口显示原图浏览。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 916~1128 行中的 `Dir_Search_Show()`，以及第 1376~1395 行中的 `Show_Pic()`。
    - 实现思路：
      * `Dir_Search_Show()` 中使用系统调用 `opendir()` (第929行) 和 `readdir()` (第959行) 遍历指定路径下的文件。
      * 通过 `Check_Valid_Pic()` 校验后缀为 `.png` 或 `.gif` 的图片文件。
      * 调用 `lv_obj_add_event_cb(file_btn, Show_Pic, LV_EVENT_SHORT_CLICKED, dii)` 绑定点击事件，当用户点击该图片按钮时触发 `Show_Pic()`，并在 `pic_win_timer_cb()` (第1244~1370行) 中动态创建全屏的图片预览弹窗展示原图。

[✓] 2. 图片文件图标则显示新窗口展示图片。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 1055~1066 行。
    - 实现思路：
      * 在目录检索时，如果文件是有效图片，使用 `lv_label_set_text(icon_lab, LV_SYMBOL_IMAGE)` 设置其图标为 LVGL 的内置图片符号（第1055行）。
      * 将按钮背景设为天蓝色 `lv_color_make(135, 206, 250)`（第1057行）作为区分，并为该按钮绑定 `Show_Pic` 点击回调，触发图片弹窗。

[✓] 3. 显示目录检索列表，可点击目录按钮切换目录显示。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 1097~1109 行（列表按钮添加）及第 880~909 行（事件处理 `Update_Dir_List()`）。
    - 实现思路：
      * 检索中若检测到是文件夹（`DT_DIR`，第1085行），在左侧 `dir_list`（QList 风格列表）中添加子目录选项：`lv_list_add_btn(p_dbi->dir_list, LV_SYMBOL_DIRECTORY, eq->d_name)`。
      * 绑定事件 `lv_obj_add_event_cb(dir_btn, Update_Dir_List, LV_EVENT_SHORT_CLICKED, dii)`。
      * 当点击目录按钮时，触发 `Update_Dir_List()` 启动淡出动画，随后定时器调用 `spinner_timer_cb()` (第830~874行) 释放旧目录链表空间（调用 `Destroy_List` 彻底释放防止内存泄露），清理右侧文件显示容器，读取新目录并重新调用 `Dir_Search_Show()` 渲染，最后开启淡入动画。

[✓] 4. 项目分为四个界面：主界面，目录列表文件显示界面，图片显示界面，退出界面。
    - 对应源码：`dir_file_list/dir_file_list.c` 
      * 主界面/列表文件界面：`Show_Dirfile_Windows()` (第564~811行) 统一初始化并构建左侧目录列表 `dir_list` 和右侧网格布局容器 `file_container`。
      * 图片显示界面：`pic_win_timer_cb()` (第1244~1370行) 创建带防误触半透明遮罩层 `bg_mask` 和子级窗口 `win` 的全屏图片浏览弹窗。
      * 退出界面：`Exit_Pro()` (第1559~1603行) 渲染纪念碑谷风格退出页 `goodbye_page`，展示 See you next time! 提示文字，延迟1秒退出。

-------------------------------------------------------------------------
【难度等级二 (80~90分，基于难度一升级过渡特效)】
-------------------------------------------------------------------------
[✓] 1. 每一个界面切换使用特效切换：淡入淡出、从下往上等。
    - 对应源码：`dir_file_list/dir_file_list.c`
      * 目录切换淡入淡出：在 `Update_Dir_List()` 阶段二（第893~906行）启动旧页面淡出动画，让容器透明度从 255 渐变到 0 (`lv_anim_set_values(&a, 255, 0)`)；在 `spinner_timer_cb()` 阶段三（第858~870行）启动新数据淡入动画，从 0 渐变到 255。
      * 图片弹窗侧滑与回弹：在 `pic_win_timer_cb()` 步骤5（第1359~1370行）为弹窗 `win` 绑定滑入动画，使用物理回弹效果 `lv_anim_path_overshoot`，X 轴从 `-600` 滑入至 `100`。
      * 图片翻页垂直顶替切换：在 `Page_Btn_Event()` (第1453~1507行) 中，旧图片根据翻页方向被向上"顶"飞出屏幕外上方 `-400`（或向下"压"出屏幕外下方 `400`），并自动回收内存；新图片则从外侧相对飞入中间，利用缓动刹车 `lv_anim_path_ease_out` 产生平滑停顿。

[✓] 2. 进界面进入功能界面是使用bar控件加载(自己需要拓展线程)或者gif动画显示(就不需要淡入淡出等特点)。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 889~892 行，以及第 1381~1389 行。
    - 实现思路：
      * 目录切换加载提示：点击目录后立即调用 `lv_spinner_create(lv_scr_act(), 1000, 60)` 在屏幕正中放置一个加载圆圈转盘，延迟 600ms 后在 `spinner_timer_cb` 中将其删除，为后续界面的绘制争取了缓冲时间。
      * 图片预览加载提示：点击图片图标时，先调用 `lv_spinner_create()` 并在此时将转盘指示器颜色更改为浅黄色 `lv_color_make(255, 255, 150)` 突出设计质感，转动 1000ms 后才在 `pic_win_timer_cb()` 中移除加载圈并弹出图片窗口。

[✓] 3. 在左边的list第一个条目项或者上面的位置，显示当前所在的路径。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 918~926 行。
    - 实现思路：
      * 顶部的状态信息区（灵动岛样式）包含了 `p_dbi->path_label`（在 `Show_Dirfile_Windows()` 中初始化）。
      * 进入 `Dir_Search_Show()` 时，调用 `lv_label_set_recolor(p_dbi->path_label, true)` 开启重色功能。
      * 通过 `sprintf(island_show_path, "#FFFF00 Local path:# #00FF00 %s#", obj_dir)` 将前缀和当前绝对路径强制渲染为亮黄色和亮绿色高亮展示。

-------------------------------------------------------------------------
【难度等级三 (90~100分，基于难度一、二完整细节适配)】
-------------------------------------------------------------------------
[✓] 1. 在图片预览界面中显示该图片的完整路径；在主功能界面显示当前目录下的图片文件总张数。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 1298, 1520 行（路径），及第 955, 1051, 1117 行（张数）。
    - 实现思路：
      * 弹窗上方：通过 `lv_win_add_title(win, dii->new_dir_path)` 将链表节点中的绝对路径赋予窗口标题。在翻页时，调用 `lv_label_set_text(pvi->title_label, target_node->new_dir_path)` 以便在当前窗口直接刷新文字，不再重复生成标题栏控件。
      * 主功能界面：在 `Dir_Search_Show` 开始处初始化 `pic_count = 0`，遍历期间每有一张有效图片，`pic_count++`，最后通过 `lv_label_set_text_fmt(p_dbi->pic_count_label, "#0000FF Images count: # #0000FF %d#", pic_count)` 广播并更新在界面右上角。

[✓] 2. 获取开发板时间用lab显示（自己需要拓展线程）。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 478~495 行中的 `rtc_thread_func()`（独立线程）和第 498~506 行中的 `update_time_cb()`（LVGL定时器）。
    - 实现思路：
      * 采用**无锁多线程共享缓冲区**设计。
      * 主线程在 `Show_Dirfile_Windows()` (第706行) 中调用 `pthread_create(&tid, NULL, rtc_thread_func, NULL)` 启动后台独立线程。
      * 线程内部死循环中，调用系统 API `time()` 和 `localtime()` 获取系统当前的 RTC 时间，并通过 `sprintf(g_time_str, ...)` 直接写入共享黑板 `g_time_str`（第489行），每秒调用一次 `sleep(1)`。
      * LVGL 侧（第716行）注册 `lv_timer_create(update_time_cb, 500, NULL)`，每 500ms 刷新一次并将 `g_time_str` 读取到 `time_label` 上，保证了 UI 操作都在 LVGL 主线程中安全处理。

[ ] 3. 文件检索功能。
    - 当前状态：未实现。
    - 局限性说明：代码当前不支持拼音或文本框输入模糊检索本地的特定图片，后续可在 UI 顶部栏的搜索框及中文键盘模块扩展此机制。

[✓] 4. 在图片原图中新增两个按钮实现上一张下一张图片显示。
    - 对应源码：`dir_file_list/dir_file_list.c` 第 1326~1356 行（创建按钮）及第 1403~1522 行（翻页逻辑 `Page_Btn_Event()`）。
    - 实现思路：
      * 数据结构设计：每一个被读取出来的图片节点均包含 `next` 和 `prev` 指针。在 `Add_List_Node()` (第1134~1169行) 中将新小弟和老大 `head` 进行连接，形成双向循环闭环大圈。
      * 按钮绑定：在图片弹窗 `cont` 的右侧，上下对齐放置两个圆形的半透明悬浮按钮，符号分别设为 `LV_SYMBOL_UP` 和 `LV_SYMBOL_DOWN`，均绑定 `Page_Btn_Event()` 短按回调。
      * 翻页调度：点击向下翻页时，顺着 `next` 指针寻找下一个 `PNG` 或 `GIF` 节点；点击向上翻页时，顺着 `prev` 指针寻找上一个节点，并且特别做好了**防雷保护**：即如果往前找遇到虚拟链表头 `head` 必须直接跳过，防止读取其空成员导致段错误。
      * 找到目标节点后，启动旧图片飞出、新图片飞入的级联动画，并使用 `lv_obj_move_foreground` 强制将两个悬浮翻页按钮重新移回最前层，避免被新画出的图片遮挡。


=========================================================================
第二期：FluxCloud 流光云盘（阶段二核心功能）
=========================================================================

-------------------------------------------------------------------------
【难度等级一 (60~70分)】
-------------------------------------------------------------------------
[√] 1. 服务器：服务器支持保存客户端上传的文件
    - 对应源码：`dir_file_list/server/server.c` 第 98~124 行中的 `handle_upload()`。
    - 实现思路：服务器接收到 `OPT_UPLOAD` 消息后，接收上传数据，并通过 IO 写入指定的文件中保存。

[√] 2. 服务器：服务器支持保存文件（文件IO保存）
    - 对应源码：`dir_file_list/server/server.c` 第 110~122 行。
    - 实现思路：使用底层系统调用 `open(path, O_WRONLY | O_CREAT | O_TRUNC, 0664)` 建立本地文件，循环读取套接字中的网络字节流数据，再通过 `write()` 持续写入磁盘，最后调用 `close()` 关闭文件。

[√] 3. 服务器：服务器支持客户端下载保存的文件
    - 对应源码：`dir_file_list/server/server.c` 第 127~156 行中的 `handle_download()`。
    - 实现思路：当客户端发送 `OPT_DOWNLOAD` 下载请求包，服务端在 `handle_download` 中打开本地存储的文件，先向客户端发送文件大小及响应头，再通过循环读取本地文件并使用 `write()` 持续写入客户端套接字。

[√] 4. 服务器：使用printf界面进行人机交互
    - 对应源码：`dir_file_list/server/server.c`。
    - 实现思路：服务端程序没有图形界面，而是通过在控制台中使用大量的标准输出 `printf` 实时打印网络监听状态、客户端接入事件、IP 及端口号、文件传输进程等。

[√] 5. 服务器：用数组保存客户端套接字
    - 历史与演进：早期 V1.0 系统为了简单起见，在全局声明了 `int client_fds[MAX]` 数组进行套接字保存。在升级到 V2.0 后面临多客户端动态接入时，为了避免数组在断开连接时产生空洞及查找瓶颈，升级为了更加弹性的**双向/单向链表结构**进行保存，支持线程安全管理。

[√] 6. 服务器：支持多客户端连接
    - 对应源码：`dir_file_list/server/server.c` 及 `threadpool.c`。
    - 实现思路：主线程负责 `listen` 及 `accept` 接入客户端。每当接入一个新连接，不再阻塞当前进程，而是生成一个新的任务包并通过 `threadpool_add_task` 投递给线程池，由子线程在后台循环读取处理。

[√] 7. 客户端：使用LVGL做界面
    - 对应源码：`dir_file_list/dir_file_list.c`。
    - 实现思路：通过集成 LVGL v8.2 框架，运用各种基础核心控件（如窗口 `lv_win`、按钮 `lv_btn`、列表 `lv_list`、文字 `lv_label`、图片 `lv_img` 等）组合拼装成流光云盘的交互面板。

[√] 8. 客户端：客户端支持把文件上传到服务器
    - 对应源码：`dir_file_list/dir_file_list.c` 第 1817~1854 行 `upload_thread`。
    - 实现思路：在本地文件按钮上长按触发 `Local_File_Long_Press_Event()`，弹窗确认后通过 `pthread_create` 启动独立上传线程。在 `upload_thread` 中，调用客户端动态库接口 `upload_file()` 进行套接字打包传输。

[√] 9. 客户端：客户端支持从服务器下载文件
    - 对应源码：`dir_file_list/dir_file_list.c` 第 1856~1908 行 `download_thread`。
    - 实现思路：在云端网格按钮上长按触发 `Cloud_File_Long_Press_Event` 确认，生成独立下载线程 `download_thread`。线程内部调用客户端网络库中的 `download_file()`，向服务端发送请求字节，将数据保存至本地。

[√] 10. 客户端：显示上传下载文件列表
    - 对应源码：`dir_file_list/dir_file_list.c`
      * 本地文件列表：通过 `Dir_Search_Show()` 实时更新右侧网格容器 `file_container`。
      * 云端文件列表：点击云盘切换选项卡后，触发 `Load_Cloud_File_List` (第2115~2323行)，向服务器发送 `OPT_LIST` 指令，把返回的文件列表通过 `strtok()` 按新行拆解，并动态在右侧画出带黄色图标的云端文件按钮。

[√] 11. 客户端：客户端支持保存下载的文件
    - 对应源码：`dir_file_list/client/client.c` 中的 `download_file()` 实现。
    - 实现思路：在网络库下载处理过程中，客户端调用本地文件系统 API 在预设路径（本地存储 CLOUD_ROOT）下创建对应文件，读取套接字包将收到的字节流写入本地。

-------------------------------------------------------------------------
【难度等级二 (70~90分)】
-------------------------------------------------------------------------
[√] 1. 服务器新增功能：用链表保存客户端IP和套接字
    - 对应源码：`dir_file_list/server/server.c` 第 8~61 行。
    - 实现思路：
      * 设计了链表节点 `struct client_node` 保存每一个在线客人的 IP 地址、端口和 `client_fd` 套接字。
      * 使用全局 `client_list_head` 统一管理。
      * 提供了线程安全的增删改查函数：`add_client()`、`remove_client()` 和 `show_clients()`，在链表节点变更时均使用互斥锁 `pthread_mutex_lock(&list_lock)` 保护多线程安全。

[√] 2. 服务器新增功能：Makefile
    - 对应源码：`dir_file_list/server/Makefile`。
    - 实现思路：手写支持模块化编译的 Makefile，将 `server.c` 编译为可执行程序，自动跟踪头文件变化并进行中间 `.o` 清理。

[√] 3. 服务器新增功能：动态库 (libserver.so)
    - 对应源码：`dir_file_list/server/Makefile` 中关于 `libserver.so` 的生成目标。
    - 实现思路：利用 GCC 编译参数 `-fPIC -shared` 将服务器的核心业务功能与依赖的开源 JSON 解析库 `cJSON` 统一编译打包成一个共享动态链接库 `libserver.so`。

[√] 4. 客户端新增功能：使用LVGL做界面
    - 对应源码：`dir_file_list/dir_file_list.c`。
    - 实现思路：开发板显示端通过集成了高级布局 Tabview 选项卡，划分出“本地流光文件夹”和“云端备份文件柜”两大板块。顶栏包含网络状态指示灯、WiFi 图标、城市天气显示、RTC 实时小时钟等，底层集成拼音输入法，提供了完整的全真云盘交互界面。

[√] 5. 客户端新增功能：http获取显示天气
    - 对应源码：`dir_file_list/dir_file_list.c` 第 2551~2629 行 `Get_Weather_Thread()`。
    - 实现思路：
      * 主界面渲染后生成独立的天气网络更新线程。
      * 线程内部进行网络全链路处理：
        1) 调用 `gethostbyname(api.seniverse.com)` 域名 DNS 解析（第2557行）。
        2) 建立套接字并连接 80 端口（第2564~2586行）。
        3) 组装 HTTP GET 报文：`sprintf(request, "GET /v3/weather/now.json?key=%s&location=%s... HTTP/1.1\r\nConnection: close\r\n\r\n")`（第2594行）并使用 `write()` 投递。
        4) 阻塞等待循环调用 `read()` 接收心知天气服务器回送的报文（第2614行）。
        5) 使用 `strstr(response, "\r\n\r\n")` 剔除 HTTP 头，提取干净的 JSON 字符串（第2635行）。
        6) 通过 `cJSON_Parse()` 解析出当前城市名称、天气状况（晴、雨、雪等）和实时温度。
        7) 自主编写 `get_weather_symbol()` 根据天气文字返回对应的符号代号（如雨天返回 `LV_SYMBOL_CHARGE` 闪电，雪天返回 `LV_SYMBOL_IMAGE` 图片等），更新到 UI 状态栏中。

[√] 6. 客户端新增功能：动态库 (libclient.so)
    - 对应源码：`dir_file_list/client/Makefile` 及 `client.c`。
    - 实现思路：将客户端所有的网络通信库函数（`init_net()`、`send_pkg()`、`upload_file()`、`download_file()`、`list_files()` 等）及依赖的 `cJSON` 代码，使用 GCC 参数统一打成动态链接库 `libclient.so` 供客户端主程序 `main.c` 链接使用。

[√] 7. 客户端新增功能：Makefile
    - 对应源码：`dir_file_list/Makefile` 以及 `dir_file_list/client/Makefile`。
    - 实现思路：编写自动化多目录 Makefile 脚本，保证库代码修改时能够自动重新生成 `libclient.so` 并完成客户端主程序的依赖性构建。

-------------------------------------------------------------------------
【难度等级三 (90~100分)】
-------------------------------------------------------------------------
[√] 1. 服务器新增功能：使用线程池
    - 对应源码：`dir_file_list/server/threadpool.c` 中的 `threadpool_init()`, `thread_routine()`, `threadpool_add_task()`, `threadpool_destroy()`。
    - 实现思路：
      * 手写实现了一个经典的高并发 FIFO 线程池。
      * 初始化：`threadpool_init(5)` 在堆区申请 `threadpool_t` 空间，创建 5 个子线程常驻后台并运行 `thread_routine` 线程主体函数，创建互斥锁 `lock` 与条件变量 `cond`。
      * 调度与挂起：当任务列表 `task_list` 为空时，工作线程调用 `pthread_cond_wait(&pool->cond, &pool->lock)` 进入就绪休眠状态。
      * 任务投递：当 accept 新连接时，主线程创建 `task_t` 任务包，通过尾插法添加到队尾，调用 `pthread_cond_signal()` 唤醒一个工作线程执行该客户端任务 `client_service`。
      * 优雅销毁：在 `threadpool_destroy` 中将 `shutdown` 设为 true，使用 `pthread_cond_broadcast` 广播唤醒所有工作线程，调用 `pthread_join` 等待所有子线程退出后，安全释放所有动态分配的线程、互斥锁和堆内存。

[√] 2. 服务器新增功能：文件IO保存客户端用户名密码
    - 对应源码：`dir_file_list/server/server.c` 第 224~305 行 `handle_register()` 与 `handle_login()`。
    - 实现思路：
      * 用户注册：服务器接收到 `OPT_REGISTER` 包，利用文件 IO 只读打开本地用户名仓库：`fopen("users.txt", "r")`。
      * 查重：逐行读取并校验是否已有该用户名。若无重复，则以追加方式写入新注册的用户信息 `fopen("users.txt", "a")`，保存格式为 `用户名 密码`。
      * 用户登录：服务器接收 `OPT_LOGIN` 包，打开 `users.txt` 并遍历比对密码哈希/明文。若用户名密码完全一致则返回登录成功。

[√] 3. 客户端新增功能：客户端登录注册功能
    - 对应源码：`dir_file_list/dir_file_list.c` 第 228~437 行。
    - 实现思路：
      * 客户端启动后，在 `Show_Loading_Screen` 结束后不进入主功能，而是优先载入登录注册界面，界面包含 `Username` 和 `Password` 两个 `lv_textarea` 文本框。
      * 点击注册或登录按钮后，将文本框内内容读取出来并组装成包含 `OPT_LOGIN` 或 `OPT_REGISTER` 的 `packet_t` 协议包发送给服务器，等待服务器返回校验包确认后才准许进入云盘主界面。

[√] 4. 客户端新增功能：中文输入法
    - 对应源码：`dir_file_list/dir_file_list.c` 第 169~226 行。
    - 实现思路：
      * 客户端集成了百文网 `lv_100ask_pinyin_ime` 拼音输入法库，并预先声明 `static lv_obj_t * kb = NULL` 共享键盘指针。
      * 当用户点击登录输入框或天气城市输入框触发 `ta_event_cb` 聚焦事件时，调用输入法库 `lv_100ask_pinyin_ime_create` 动态创建中文拼音拼写引擎，将键盘父节点设为 `lv_layer_top()` 置顶防切割，绑定文本框后自动显示键盘。
      * 用户通过点击字母，拼音输入法计算出汉字候选词列表，点击候选汉字即可完成中文文字的写入。
# =========================================================================
"""

# ----------------- Aura V4.0 Content -----------------
p3_content = """# =========================================================================
#  Aura V4.0 - 项目功能逐条复盘（含AI扩展与官方核对表适配）
#  微光智控餐饮终端(Aura) 阶段项目三
# =========================================================================

此文档根据官方下发的《项目进度功能核对表 - 微光智控餐饮终端(Aura)》逐条整理，全面核对并复盘了具体代码的实现细节、源码文件位置、以及具体行号，便于面试前查阅与快速回顾。

=========================================================================
【难度等级一 (60~80分)】
=========================================================================
[✓] 1. <<服务器(Win)>> 支持客户端上传的用户订单 (包含菜品、桌号等信息，JSON解析)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 424~452 行中的 `handleOrderSubmit()`。
    - 实现思路：
      * 当客户端提交订单时，服务端在 `onSocketReadyRead()` 中读取 JSON 行（以 `\\n` 分割数据帧，第369~382行），并通过 `QJsonDocument::fromJson` 反序列化。
      * 在 `handleOrderSubmit()` 中解析出客户端传来的 `table_num` (桌号)、`people` (人数)、`total_price` (总价) 以及 `items` 菜品明细数组。

[✓] 2. <<服务器(Win)>> 支持把菜单下发给客户端 (查询数据库并拼装JSON数组)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 402~422 行中的 `sendMenuTo()`。
    - 实现思路：
      * 客户端发送 `"get_menu"` 网络请求后，服务端响应 `sendMenuTo()`。
      * 内部通过 SQL 检索语句 `SELECT id, name, price, stock, image_path, description FROM menu ORDER BY id` 查询菜单信息。
      * 遍历结果集构建 `QJsonArray` 并封装成 JSON 对象，调用 `sendJson` 顺着 TCP Socket 写回给客户端。

[✓] 3. <<服务器(Win)>> 支持用数据库视图显示用户订单 (QTableView + QSqlTableModel)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 121~131 行（初始化模型）及第 180~199 行（视图映射）。
    - 实现思路：
      * 在数据库初始化时，实例化 `orderModel = new QSqlTableModel(this, db)`，指定映射数据表为 `"orders"`。
      * 设置视图修改策略为 `QSqlTableModel::OnManualSubmit`。
      * 随后将后台监控页面的 `orderView` (QTableView) 的数据源绑定至该模型 `orderView->setModel(orderModel)`，实现数据的可视化网格监控。

[✓] 4. <<服务器(Win)>> 支持用数据库视图显示菜单库存 (QTableView + QSqlTableModel)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 110~120 行（初始化模型）及第 204~219 行（视图映射）。
    - 实现思路：
      * 实例化 `menuModel = new QSqlTableModel(this, db)` 并绑定 `"menu"` 菜单库存数据表。
      * 在后台界面的“菜单库存管理” Tab 选项卡中，调用 `menuView->setModel(menuModel)` 将列表网格与数据库模型绑定，实现直观的菜品名称、价格、库存和描述监控。

[✓] 5. <<服务器(Win)>> 数据库支持增删改查的操作 (QSqlDatabase + QSqlQuery，实现后台管理)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 52~131 行（数据库初始化建表与预置数据），及第 327~345 行中的 CRUD 回调函数。
    - 实现思路：
      * 初始化：在 `initDatabase()` 中调用 `QSqlDatabase::addDatabase("QSQLITE")` 新建并打开名为 `AuraDB.db` 的本地 SQLite 数据库。
      * 增删改查：
        1) 新增菜品：`onAddMenu()` 触发 `menuModel->insertRow(menuModel->rowCount())` 在模型末尾追加新行，用户可在表格内直接编辑。
        2) 删除选中：`onDeleteMenu()` 根据当前选中的行索引调用 `menuModel->removeRow(currentRow)`。
        3) 提交同步：`onSubmitMenu()` 统一调用 `menuModel->submitAll()` 将所有挂起的修改（包括增改删）通过事务一次性同步到底层 SQLite 数据库中。
        4) 撤销修改：`onRevertMenu()` 触发 `menuModel->revertAll()` 撤回所有未同步的更改。

[✓] 6. <<客户端(ARM)>> 获取服务器的菜单 (QTcpSocket 连接并解析返回数据)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 522~533 行 (`initNetwork()`), 第 587~604 行 (`onReadyRead()`), 第 637~642 行 (`requestMenu()`)。
    - 实现思路：
      * 连接服务器：客户端调用 `tcpSocket->connectToHost(ip, port)` 并在连接成功后发送 `{type: "get_menu"}` 请求。
      * 数据解析：当服务端回写菜单 JSON 数据时，客户端触发 `onReadyRead()` 接收流数据，通过换行符 `\\n` 切分出完整的 JSON 行。
      * 通过 `QJsonDocument::fromJson` 解析出包含菜品属性的数组，路由给 `OrderPage` 的模型加载器。

[✓] 7. <<客户端(ARM)>> 并且把菜单显示到listwidget自定义条目项中 (自定义 Widget 塞入 QListWidget)
    - 对应源码与高版本演进：
      * 早期 V1.0 系统为了展示复杂的菜品（包含图片、加减按钮和描述），声明了 `QListWidget`，并对每一个菜品都使用 `QListWidgetItem` 加 `setItemWidget()` 塞入一个复杂的自定义 `QWidget` 节点。
      * 此方案虽可运行，但因在嵌入式开发板上动态绘制大量重量级 `QWidget` 极易导致界面严重卡顿、切换闪烁和极高内存消耗。
      * 在升级到 V2.0 和最终 V4.0 系统中，对此进行了重构，抛弃了低效的 `QListWidget` 方案，升级为了**高扩展性的 MVC 模型/视图架构**：使用 `QListView` 作为容器，利用轻量级自定义 `MenuModel` 存储数据，并自主编写 `MenuDelegate` (QStyledItemDelegate) 实现轻量级图形绘制（具体见难度三第18项），实现了完美的性能优化。

[✓] 8. <<客户端(ARM)>> 自定义条目中可选择菜的数量 (QSpinBox 改变数量并触发信号)
    - 对应源码与高版本演进：
      * 在早期方案中，通过在自定义条目的 `QWidget` 里塞入 `QSpinBox`，监听其 `valueChanged()` 信号来修改对应菜品的点单数量。
      * 在升级后的高效率 MVC 架构中，该功能在 `Aura_Client/menudelegate.cpp` 第 181~207 行的 `editorEvent()` 中实现。
      * 委托拦截用户的鼠标/触屏释放事件 `QEvent::MouseButtonRelease`，通过判定点击坐标是否位于 `plusBtnRect` (加号按钮) 或 `minusBtnRect` (减号按钮) 的矩形包围盒内。
      * 坐标撞击成立后，调用模型 `model->setData(index, newQty, QtyRole)` 改变对应菜品的数量，模型随后发送 `dataChanged` 信号刷新页面，不留任何多余重量级子控件。

[✓] 9. <<客户端(ARM)>> 支持客户端点菜的详细订单并且计算总价 (遍历数据结构实时计算金额)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 422~434 行中的 `OrderPage::onModelQtyChanged()`。
    - 实现思路：
      * 在 `OrderPage` 中声明了 `QMap<int, CartItem> m_cart` 来存储被选中的菜品（键为菜品 ID）。
      * 当用户通过 delegate 修改菜品数量时，触发 model 发送信号并路由至 `onModelQtyChanged()` 回调。
      * 此时，将修改后的菜品及对应数量、价格更新至 `m_cart` 购物车容器（若数量减为0则从 `m_cart` 中移出）。
      * 随后重新遍历 `m_cart` 所有项目，累加 `price * qty` 计算总金额并实时显示在底栏的 `lblTotal` 标签上。

[✓] 10. <<客户端(ARM)>> 支持把详细订单和总价和餐桌号上传到服务器 (打包为JSON并通过 Socket 发送)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 669~697 行中的 `submitOrder()`。
    - 实现思路：
      * 当用户在购物车结算框中点击确认下单后，触发 `submitOrder()`。
      * 构造一个 `QJsonObject` 主请求包，写入字段 `type = "submit_order"`, `table_num = m_tableNum`, `people = guestCount`, `total_price = totalPrice`。
      * 遍历 `m_cart` 购物车，过滤只保留 `qty > 0` 的菜品，拼装成包含 `{dish_id, qty}` 的 `QJsonArray` 并存入主包中的 `items` 键下。
      * 最后用 `QJsonDocument(req).toJson(QJsonDocument::Compact)` 压成单行字节流，末尾追加 `\\n` 作为帧尾，通过套接字写回给服务端。

[✓] 11. <<客户端(ARM)>> 支持选择就餐人数 (界面提供选择并随订单上传)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 32, 67~77, 100~102 行（迎宾选择页 `WelcomePage`），及第 691 行（订单上传）。
    - 实现思路：
      * 迎宾页提供了 `spinGuests` (QSpinBox)，范围限定在 1 至 20 人（第68行）。
      * 用户点击“开始点餐”时，该数值跟随信号 `startOrdering(spinGuests->value())` 路由到 `ClientWindow::onStartOrdering()`。
      * 主窗口接收人数后，将其记录到后台，并调用 `orderPage->setGuestCount(guestCount)` 初始化点餐主页；在最后订单结算上传时通过 `submitOrder` 中的 `people` 字段同步上传给服务端。

=========================================================================
【难度等级二 (80~90分)】
=========================================================================
[✓] 12. <<服务器(Win)>> 用定时器显示系统时间 (QTimer 实时更新)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 306~311 行。
    - 实现思路：
      * 在 `initTimeAndWeather()` 注册 `timeTicker = new TimeTicker(this)`。
      * 内部封装了 `QTimer`，每 1000 毫秒发出一次时间刷新信号。
      * 将该信号与底栏的 `lblTickTime` 关联，显示 12 小时制/24 小时制的秒级系统时间。

[✓] 13. <<客户端(ARM)>> 用定时器显示系统时间 (QTimer 实时更新)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 657~662 行。
    - 实现思路：
      * 逻辑与服务端完全对应，在 `initTimeAndWeather()` 中初始化 `timeTicker = new TimeTicker(this)`。
      * 绑定刷新回调，将格式化后的当前系统时间显示在客户端右下角底部状态栏。

[✓] 14. <<客户端(ARM)>> 购物车功能 (独立界面或侧边栏，展示已选菜品清单并支持修改/删除)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 148~329 行的 `CartDialog` 类，以及 `OrderPage::onCartClicked()`。
    - 实现思路：
      * 当用户在点餐页点击右下角的“购物车”图标时，触发 `onCartClicked()`（第112行）。
      * 将当前的购物车记录 `m_cart` 及总金额传入并实例化 `CartDialog` 模态对话框。
      * 该对话框内渲染了所有当前选购的菜品名称、单价及已选份数，并配备“确认支付/取消下单”操作，实现隔离结算。

=========================================================================
【难度等级三 (90~100分)】
=========================================================================
[✓] 15. <<服务器(Win)>> 用线程显示时间 (QThread 子线程发信号更新 UI)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 299~304 行，以及 `timethread.h`。
    - 实现思路：
      * 创建继承自 `QThread` 的自定义时间工作子线程 `TimeThread`。
      * 在其重载的 `run()` 主循环函数中，每隔 500ms 睡眠后，向主线程发射信号并投递当前系统时间的字符串：`emit timeUpdated(QDateTime::currentDateTime().toString("yyyy/MM/dd hh:mm:ss"))`。
      * 服务端主窗口接收该信号并更新至顶部状态栏 `lblTime` 展示。

[✓] 16. <<服务器(Win)>> http获取天气 (QNetworkAccessManager 调用外部API)
    - 对应源码：`Aura_Server/serverwindow.cpp` 第 313~322 行，以及 `weatherfetcher.cpp`。
    - 实现思路：
      * 服务端后台集成 `WeatherFetcher` 实例，内部使用 Qt 官方网络库 `QNetworkAccessManager` 发起异步 HTTP GET 请求。
      * 异步访问外部公开天气接口，在返回的回复信号 `finished` 中提取 JSON 格式的天气内容，用 `QJsonDocument` 提取实时温度及晴雨汉字，返回给主窗体展现在右上角。

[✓] 17. <<客户端(ARM)>> 用线程显示时间 (同服务器第15点)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 649~654 行。
    - 实现思路：
      * 客户端子线程 `TimeThread` 在后台保持运行，发射秒级信号，并通过槽机制在 `OrderPage::updateTimeLabel()` 中将时间实时展现在顶部信息条。

[✓] 18. <<客户端(ARM)>> 把listwidget换成其他拓展控件 (重写 MVC 架构，QListView + QStyledItemDelegate，解决性能问题)
    - 对应源码：
      * 核心列表类：`Aura_Client/menumodel.cpp` (QAbstractListModel) 第 1~115 行。
      * 核心绘制委托类：`Aura_Client/menudelegate.cpp` (QStyledItemDelegate) 第 1~208 行。
      * 视图装载：`Aura_Client/clientwindow.cpp` 第 339~412 行的 `OrderPage::initUI()`。
    - 升级后实现细节：
      * 模型层 `MenuModel`：继承自 `QAbstractListModel`，内部使用 `QList<DishData> m_items` 作为低开销的核心数组。重写了 `rowCount()` 用于返回行数，以及 `data()` 用于根据指定的自定义 Role (如 `NameRole`, `PriceRole`, `QtyRole` 等) 返回菜品属性。重写了 `setData` 以处理数量修改并通知视图刷新。
      * 委托层 `MenuDelegate`：重写了 `paint()`，使用轻量级 `QPainter` 在指定的 `option.rect` 坐标范围内手画所有图形，包括：圆角餐点背景卡片（使用 `QPainterPath` 绘制）、菜品原图（第72x72像素自动缩放）、菜品名（14pt粗体）、价格（12pt红色字体）、描述（10pt灰色字体）、以及在右下角精确手绘的圆形加减数量操作按钮。没有实例化任何多余的 QWidget，不仅帧率达 60fps 以上极度流畅，还能无缝支持鼠标滑动、触控滚动和 hover 动态微光悬停特效。

[✓] 19. <<客户端(ARM)>> http获取天气 (同服务器第16点)
    - 对应源码：`Aura_Client/clientwindow.cpp` 第 664~667 行，及 `weatherfetcher.cpp`。
    - 实现思路：
      * 客户端利用 `WeatherFetcher` 在初始化后发起网络 DNS 拦截并向接口发送 HTTP GET 报文。
      * 异步成功后通过槽函数将解析出来的“广州 晴 31°C”等字眼通过信号同步传送给点餐主页的 `lblWeather` 进行置顶高亮展示。
# =========================================================================
"""

# Write files
with open(p2_txt_path, "w", encoding="utf-8") as f:
    f.write(p2_content)
print(f"Written {os.path.basename(p2_txt_path)}")

with open(p3_txt_path, "w", encoding="utf-8") as f:
    f.write(p3_content)
print(f"Written {os.path.basename(p3_txt_path)}")

print("All txt files written successfully!")
