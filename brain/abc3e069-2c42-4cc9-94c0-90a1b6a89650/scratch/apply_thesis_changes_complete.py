import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Clean concrete version numbers from technology names
    version_map = {
        "Vue 3": "Vue",
        "Spring Boot 2.7.6": "Spring Boot",
        "MySQL 5.7": "MySQL",
        "Redis 7": "Redis",
        "JDK 17": "JDK",
        "Maven 3.9": "Maven",
        "Node.js 22": "Node.js",
        "npm 10.9": "npm",
        "JMeter 5.5": "JMeter",
        "Prometheus 2.52": "Prometheus",
        "Grafana 10.4": "Grafana",
        "Loki 2.9": "Loki"
    }
    
    for old, new in version_map.items():
        content = content.replace(old, new)
        
    # Double check for other leftovers (like Vue 3 in the middle of a sentence)
    content = content.replace("Vue 3", "Vue")
    
    # 2. Add explicit referencing sentences above/below figures/tables
    
    # Table 1
    content = content.replace(
        "（1）用户表（user）：用户表主要存储平台用户的账号、加盐密码、昵称、头像、平台角色以及审计时间等。\n表1  用户表（user）",
        "（1）用户表（user）：用户表主要存储平台用户的账号、加盐密码、昵称、头像、平台角色以及审计时间等，具体的表结构设计如表1所示。\n表1  用户表（user）"
    )
    
    # Table 2
    content = content.replace(
        "（2）图片表（picture）：图片表主要记录多模态图像的存储路径、名称、分类与JSON标签、图片尺寸像素、文件大小以及所属空间和人工审核状态。\n表2  图片表（picture）",
        "（2）图片表（picture）：图片表主要记录多模态图像的存储路径、名称、分类与JSON标签、图片尺寸像素、文件大小以及所属空间和人工审核状态，具体的表结构设计如表2所示。\n表2  图片表（picture）"
    )
    
    # Table 3
    content = content.replace(
        "（3）空间表（space）：设计了最大容量和最大数量字段，以支持个人私有空间与多租户团队空间的存储配额限额控制。\n表3  空间表（space）",
        "（3）空间表（space）：设计了最大容量和最大数量字段，以支持个人私有空间与多租户团队空间的存储配额限额控制，具体的表结构设计如表3所示。\n表3  空间表（space）"
    )
    
    # Table 4
    content = content.replace(
        "（4）空间成员表（space_user）：保存用户与空间的映射关系，记录用户在特定空间中的角色（管理员、编辑者、浏览者），用以支持Sa-Token的细粒度RBAC鉴权。\n表4  空间成员表（space_user）",
        "（4）空间成员表（space_user）：保存用户与空间的映射关系，记录用户在特定空间中的角色（管理员、编辑者、浏览者），用以支持Sa-Token的细粒度RBAC鉴权，具体的表结构设计如表4所示。\n表4  空间成员表（space_user）"
    )
    
    # Figure 1
    content = content.replace(
        "系统功能模块划分为用户模块、空间模块、管理模块、AIGC模块与图片模块。系统功能模块图如图1所示。",
        "系统功能模块划分为用户模块、空间模块、管理模块、AIGC模块与图片模块，系统的模块划分结构如图1所示。"
    )
    
    # Figure 2
    content = content.replace(
        "主体区域采用无限滚动瀑布流方式展示公开图库中的高质量多模态图像，每张图片卡片集成了快速预览、一键分享、编辑及软删除操作入口。\n图2  系统主界面",
        "主体区域采用无限滚动瀑布流方式展示公开图库中的高质量多模态图像，每张图片卡片集成了快速预览、一键分享、编辑及软删除操作入口。系统主界面展示效果如图2所示。\n图2  系统主界面"
    )
    
    # Figure 3
    content = content.replace(
        "生成任务完成后PictureService接口的uploadPicture方法把结果存入picture表并返回图片地址。\n图3  文生图界面",
        "生成任务完成后PictureService接口的uploadPicture方法把结果存入picture表并返回图片地址。文生图生成界面如图3所示。\n图3  文生图界面"
    )
    
    # Figure 4
    content = content.replace(
        "进度轮询由getTextToVideoTask端点负责，生成任务完成后返回播放视频链接。\n图4  文生视频界面",
        "进度轮询由getTextToVideoTask端点负责，生成任务完成后返回播放视频链接。文生视频生成界面如图4所示。\n图4  文生视频界面"
    )
    
    # Figure 5
    content = content.replace(
        "getImageToVideoTask方法提供进度轮询，由FileController类的uploadImageForVideo处理临时图片存储。\n图5  图生视频界面",
        "getImageToVideoTask方法提供进度轮询，由FileController类的uploadImageForVideo处理临时图片存储。图生视频生成界面如图5所示。\n图5  图生视频界面"
    )
    
    # Figure 6
    content = content.replace(
        "通过AliYunAiApi类查询任务进度，用户确认应用结果后更新picture表的数据库元数据。\n图6  图像拓展界面",
        "通过AliYunAiApi类查询任务进度，用户确认应用结果后更新picture表的数据库元数据。图像外延拓展界面如图6所示。\n图6  图像拓展界面"
    )
    
    # Figure 7
    content = content.replace(
        "ChatService服务层与外部模型交互，查询由getChatTask端点提供，成功后返回追加结果。\n图7  智能对话界面",
        "ChatService服务层与外部模型交互，查询由getChatTask端点提供，成功后返回追加结果。智能对话生成界面如图7所示。\n图7  智能对话界面"
    )
    
    # 3. Rewrite 6.2 and 6.3 perfectly
    old_test_methods = "6.2  测试方法\n　　系统采用黑盒测试策略，通过等价类划分与边界值分析设计用例，核心测试AIGC五大功能与越权防御。"
    new_test_methods = (
        "6.2  测试方法\n"
        "　　本系统采用黑盒测试策略，利用等价类划分法与边界值分析法精心设计用例，以从用户角度检验各项功能逻辑的正确性与健壮性。测试范围涵盖系统的主要业务模块，重点对文生图、文生视频、图生视频、图像拓展以及智能对话五大核心AIGC创作功能开展详尽测试。在测试执行过程中，首先进行功能测试，以验证输入参数合法性校验、业务流程完整性及异常场景的容错处理；其次进行接口测试与集成测试，确保前后端数据交互格式统一、错误码规范且状态流转符合预期；最后借助JMeter工具实施并发压力测试以评估系统响应速度与稳定性，并同步开展针对越权访问的安全性测试，从而全面确保系统达到交付标准。"
    )
    content = content.replace(old_test_methods, new_test_methods)
    
    old_test_cases = (
        "6.3  测试用例\n"
        "　　针对系统核心的文生图、文生视频、图生视频、图像拓展以及智能对话五大多模态AIGC创作功能，本研究设计了多组输入数据与边界值用例以验证功能的正确性与越权安全防御能力。具体测试用例如下：\n"
        "　　（1）文生图功能测试：测试涵盖提示词为空拦截、正常提示词与参数返回任务ID、尺寸参数非法校验拦截、随机种子越界校验拦截以及生成数量上限校验拦截。\n"
        "表5  文生图功能测试用例表\n"
        "　　（2）文生视频功能测试：包括空描述拦截、合规参数的异步创建与轮询校验、非法分辨率拦截、随机种子越界拦截以及手机竖屏等多种长宽比分辨率的通过性验证。\n"
        "表6  文生视频功能测试用例表\n"
        "　　（3）图生视频功能测试：验证未上传图片时的校验拦截、单图输入模式、首尾帧图片输入模式下的正常处理逻辑、视频时长超出范围的拦截以及非法图片地址的校验。\n"
        "表7  图生视频功能测试用例表\n"
        "　　（4）图像拓展功能测试：包括缺少主体图片ID时的拦截、合法拓展比例与偏置、拓展倍率超出范围（如大于3倍）的拦截校验、空参数拦截以及高画质拓展模式测试。\n"
        "表8  图像拓展功能测试用例表\n"
        "　　（5）智能对话功能测试：测试发送空消息拦截、未指定模型时的默认适配、单次发送超长文本的拦截、非法大模型标识的拦截以及未登录用户访问受限接口 of 防越权机制。\n"
        "表9  智能对话功能测试用例表"
    )
    
    new_test_cases = (
        "6.3  测试用例\n"
        "　　针对系统核心的文生图、文生视频、图生视频、图像拓展以及智能对话五大多模态AIGC创作功能，本研究设计了多组输入数据与边界值用例以验证功能的正确性与越权安全防御能力。\n"
        "\n"
        "6.3.1  文生图功能测试\n"
        "　　文生图功能测试涵盖提示词为空拦截、正常提示词与参数返回任务ID、尺寸参数非法校验拦截、随机种子越界校验拦截以及生成数量上限校验拦截。具体测试用例如表5所示。\n"
        "表5  文生图功能测试用例表\n"
        "\n"
        "6.3.2  文生视频功能测试\n"
        "　　文生视频功能测试包括空描述拦截、合规参数的异步创建与轮询校验、非法分辨率拦截、随机种子越界拦截以及手机竖屏等多种长宽比分辨率的通过性验证。具体测试用例如表6所示。\n"
        "表6  文生视频功能测试用例表\n"
        "\n"
        "6.3.3  图生视频功能测试\n"
        "　　图生视频功能测试验证未上传图片时的校验拦截、单图输入模式、首尾帧图片输入模式下的正常处理逻辑、视频时长超出范围的拦截以及非法图片地址的校验。具体测试用例如表7所示。\n"
        "表7  图生视频功能测试用例表\n"
        "\n"
        "6.3.4  图像拓展功能测试\n"
        "　　图像拓展功能测试包括缺少主体图片ID时的拦截、合法拓展比例与偏置、拓展倍率超出范围（如大于3倍）的拦截校验、空参数拦截以及高画质拓展模式测试。具体测试用例如表8所示。\n"
        "表8  图像拓展功能测试用例表\n"
        "\n"
        "6.3.5  智能对话功能测试\n"
        "　　智能对话功能测试包括发送空消息拦截、未指定模型时的默认适配、单次发送超长文本的拦截、非法大模型标识的拦截以及未登录用户访问受限接口的防越权机制。具体测试用例如表9所示。\n"
        "表9  智能对话功能测试用例表"
    )
    
    # Let's check if there is slightly different content (e.g. including targetContent of Sa-Token or similar)
    # We will do a robust replace that finds 6.3 and Replaces the whole block
    if old_test_cases in content:
        content = content.replace(old_test_cases, new_test_cases)
        print("Replaced 6.3 block using exact string")
    else:
        # Fallback to replace piece-by-piece
        print("Exact 6.3 block not found, doing line-by-line fallback")
        content = content.replace("（1）文生图功能测试：测试涵盖", "6.3.1  文生图功能测试\n　　文生图功能测试涵盖")
        content = content.replace("（2）文生视频功能测试：包括", "6.3.2  文生视频功能测试\n　　文生视频功能测试包括")
        content = content.replace("（3）图生视频功能测试：验证", "6.3.3  图生视频功能测试\n　　图生视频功能测试验证")
        content = content.replace("（4）图像拓展功能测试：包括", "6.3.4  图像拓展功能测试\n　　图像拓展功能测试包括")
        content = content.replace("（5）智能对话功能测试：测试", "6.3.5  智能对话功能测试\n　　智能对话功能测试包括")
        
        # Now add table references
        content = content.replace("拦截以及生成数量上限校验拦截。\n表5", "拦截以及生成数量上限校验拦截。具体测试用例如表5所示。\n表5")
        content = content.replace("多种长宽比分辨率的通过性验证。\n表6", "多种长宽比分辨率的通过性验证。具体测试用例如表6所示。\n表6")
        content = content.replace("以及非法图片地址的校验。\n表7", "以及非法图片地址的校验。具体测试用例如表7所示。\n表7")
        content = content.replace("空参数拦截以及高画质拓展模式测试。\n表8", "空参数拦截以及高画质拓展模式测试。具体测试用例如表8所示。\n表8")
        content = content.replace("防越权机制。\n表9", "防越权机制。具体测试用例如表9所示。\n表9")
        
    with open(path_txt, "w", encoding="utf-8") as f:
        f.write(content)
    print("Finished applying all edits to 稿件-v4.txt")

if __name__ == "__main__":
    main()
