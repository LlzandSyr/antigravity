import os

p3_base = r"c:\Users\86135\Desktop\面试题\阶段项目3\李怜哲+微光智控餐饮终端"

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
        
    brace_count = 0
    found_brace = False
    end_line = None
    
    for idx in range(start_line - 1, len(lines)):
        line = lines[idx]
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

p3_files_funcs = [
    ("Aura_Server/serverwindow.cpp", [
        ("initNetwork", "void ServerWindow::initNetwork()"),
        ("onNewConnection", "void ServerWindow::onNewConnection()"),
        ("onSocketReadyRead", "void ServerWindow::onSocketReadyRead()"),
        ("handleMessage", "void ServerWindow::handleMessage("),
        ("initDatabase", "void ServerWindow::initDatabase()"),
        ("sendMenuTo", "void ServerWindow::sendMenuTo("),
        ("handleOrderSubmit", "void ServerWindow::handleOrderSubmit("),
    ]),
    ("Aura_Client/clientwindow.cpp", [
        ("initNetwork", "void ClientWindow::initNetwork()"),
        ("onConnected", "void ClientWindow::onConnected()"),
        ("requestMenu", "void ClientWindow::requestMenu()"),
        ("onReadyRead", "void ClientWindow::onReadyRead()"),
        ("handleMessage", "void ClientWindow::handleMessage("),
        ("onModelQtyChanged", "void OrderPage::onModelQtyChanged("),
        ("submitOrder", "void ClientWindow::submitOrder()"),
        ("CartDialog::initUI", "void CartDialog::initUI("),
        ("OrderPage::initUI", "void OrderPage::initUI()"),
    ]),
    ("Aura_Client/menumodel.cpp", [
        ("rowCount", "int MenuModel::rowCount("),
        ("data", "QVariant MenuModel::data("),
        ("setQty", "int MenuModel::setQty("),
        ("changeQty", "int MenuModel::changeQty("),
        ("loadFromJson", "void MenuModel::loadFromJson("),
    ]),
    ("Aura_Client/menudelegate.cpp", [
        ("paint", "void MenuDelegate::paint("),
        ("editorEvent", "bool MenuDelegate::editorEvent("),
        ("plusBtnRect", "QRect MenuDelegate::plusBtnRect("),
        ("minusBtnRect", "QRect MenuDelegate::minusBtnRect("),
        ("qtyTextRect", "QRect MenuDelegate::qtyTextRect("),
    ]),
    ("Aura_Client/weatherfetcher.cpp", [
        ("fetchOnce", "void WeatherFetcher::fetchOnce()"),
        ("onReplyFinished", "void WeatherFetcher::onReplyFinished("),
    ]),
]

print("=== Phase 3 Function Ranges ===")
for rel_path, funcs in p3_files_funcs:
    filepath = os.path.join(p3_base, rel_path)
    print(f"\nFile: {rel_path}")
    for name, sig in funcs:
        res = get_function_range(filepath, sig)
        if res:
            print(f"  {name}: {res[0]}~{res[1]}")
        else:
            print(f"  {name}: Not found")
