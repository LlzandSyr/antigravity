import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Normalize line endings
    content_norm = content.replace("\r\n", "\n")
    
    # 1. Database logic structure design replacement
    db_target = """4.3.2  逻辑结构设计
　　数据库表结构设计如下所示：

表4.1  用户表（user）
字段名        数据类型     长度    是否为空     是否主键    描述
id            bigint       20      否           是          唯一标识符
userAccount   varchar      256     否           否          用户账号
userPassword  varchar      512     否           否          加盐密码
userName      varchar      256     是           否          用户昵称
userAvatar    varchar      1024    是           否          头像地址
userRole      varchar      256     否           否          平台角色
editTime      datetime     -       否           否          编辑时间
createTime    datetime     -       否           否          创建时间
isDelete      tinyint      4       否           否          逻辑删除

表4.2  图片表（picture）
字段名        数据类型     长度    是否为空     是否主键    描述
id            bigint       20      否           是          唯一标识符
url           varchar      512     否           否          图片地址
name          varchar      128     否           否          图片名称
category      varchar      64      是           否          图片分类
tags          varchar      512     是           否          JSON标签
picSize       bigint       20      是           否          文件大小
picWidth      int          11      是           否          像素宽度
picHeight     int          11      是           否          像素高度
userId        bigint       20      否           否          创建用户ID
spaceId       bigint       20      是           否          所属空间ID
reviewStatus  int          11      否           否          审核状态(0-待,1-过,2-拒)

表4.3  空间表（space）
字段名        数据类型     长度    是否为空     是否主键    描述
id            bigint       20      否           是          唯一标识符
spaceName     varchar      128     是           否          空间名称
spaceLevel    int          11      是           否          空间级别配额
spaceType     int          11      否           否          空间类型(0-私,1-团)
maxSize       bigint       20      是           否          最大容量
maxCount      bigint       20      是           否          最大数量
totalSize     bigint       20      是           否          当前已用容量
totalCount    bigint       20      是           否          当前已存数量

表4.4  空间成员表（space_user）
字段名        数据类型     长度    是否为空     是否主键    描述
id            bigint       20      否           是          唯一标识符
spaceId       bigint       20      否           否          空间ID
userId        bigint       20      否           否          用户ID
spaceRole     varchar      128     是           否          空间角色(admin/editor/viewer)"""

    db_replacement = """4.3.2  逻辑结构设计
　　系统采用MySQL作为关系型数据库。为了实现对多用户、多命名空间以及多模态图片资产的精细化治理，数据库设计了四个核心实体表，其表名与描述如下所示：
　　（1）用户表（user）：用户表主要存储平台用户的账号、加盐密码、昵称、头像、平台角色以及审计时间等。
表1  用户表（user）
　　（2）图片表（picture）：图片表主要记录多模态图像的存储路径、名称、分类与JSON标签、图片尺寸像素、文件大小以及所属空间和人工审核状态。
表2  图片表（picture）
　　（3）空间表（space）：设计了最大容量和最大数量字段，以支持个人私有空间与多租户团队空间的存储配额限额控制。
表3  空间表（space）
　　（4）空间成员表（space_user）：保存用户与空间的映射关系，记录用户在特定空间中的角色（管理员、编辑者、浏览者），用以支持Sa-Token的细粒度RBAC鉴权。
表4  空间成员表（space_user）"""

    # Normalize target/replacement
    db_target_norm = db_target.replace("\r\n", "\n")
    db_replacement_norm = db_replacement.replace("\r\n", "\n")
    
    if db_target_norm in content_norm:
        content_norm = content_norm.replace(db_target_norm, db_replacement_norm)
        print("Database structure replaced successfully!")
    else:
        print("Error: Database target structure not found")
        # Let's try flexible search
        db_start = content_norm.find("4.3.2  逻辑结构设计")
        db_end = content_norm.find("5  系统实现")
        if db_start != -1 and db_end != -1:
            content_norm = content_norm[:db_start] + db_replacement_norm + "\n\n\n" + content_norm[db_end:]
            print("Database structure replaced via boundaries!")

    # 2. Section 5 implementation replacement
    ch5_start = content_norm.find("5  系统实现")
    ch6_start = content_norm.find("6  系统测试")
    if ch5_start != -1 and ch6_start != -1:
        ch5_replacement = """5  系统实现

　　系统采用标准的前后端分离架构，基于Spring Boot与Vue 3框架搭建而成。为了确保系统功能的连贯性与论证的严密性，本章将重点介绍系统的主界面以及核心多模态AIGC创作功能的具体实现。

5.1  系统主界面实现
　　系统主界面（图库首页）是用户访问系统的核心入口。前端基于响应式网格布局设计，能够自动适配不同分辨率的终端屏幕。主界面上方为全局导航栏与多维度筛选组件，支持按关键字、图片分类和多个自定义标签进行组合检索；主体区域采用无限滚动瀑布流方式展示公开图库中的高质量多模态图像，每张图片卡片集成了快速预览、一键分享、编辑及软删除操作入口。
图2  系统主界面

5.2  多模态AIGC创作功能实现
　　5.2.1  文生图功能实现：用户在文生图页面填写提示词、尺寸、种子和生成数量后提交，系统由PictureController类的createTextToImageTask方法异步创建任务并返回任务标识，服务层使用AliYunAiApi类与外部模型进行交互。生成任务完成后PictureService接口的uploadPicture方法把结果存入picture表并返回图片地址。
图3  文生图界面
　　5.2.2  文生视频功能实现：用户在文生视频页面输入文本描述并设置参数后提交，系统由TextToVideoController类的createTextToVideoTask方法接收并调用服务层创建任务，进度轮询由getTextToVideoTask端点负责，生成任务完成后返回播放视频链接。
图4  文生视频界面
　　5.2.3  图生视频功能实现：用户在图生视频页面上传图片并设置时长与帧率后提交，系统由ImageToVideoController类的createImageToVideoTask方法调用异步服务，getImageToVideoTask方法提供进度轮询，由FileController类的uploadImageForVideo处理临时图片存储。
图5  图生视频界面
　　5.2.4  图像拓展功能实现：用户在图片详情页选择图像外延参数后发起生成任务，系统由PictureController类的createPictureOutPaintingTask方法创建任务，通过AliYunAiApi类查询任务进度，用户确认应用结果后更新picture表的数据库元数据。
图6  图像拓展界面
　　5.2.5  智能对话功能实现：用户在智能对话页面输入聊天消息发起对话，系统由ChatController类的createTask方法创建异步任务，将中间状态写入Redis，ChatService服务层与外部模型交互，查询由getChatTask端点提供，成功后返回追加结果。
图7  智能对话界面

"""
        content_norm = content_norm[:ch5_start] + ch5_replacement + content_norm[ch6_start:]
        print("Chapter 5 implementation sections replaced successfully!")
    else:
        print("Error: Chapter 5 or Chapter 6 boundaries not found")

    # 3. Chapter 6.3 Test cases table replacement
    ch63_start = content_norm.find("6.3  测试用例")
    ch64_start = content_norm.find("6.4  测试结论")
    if ch63_start != -1 and ch64_start != -1:
        ch63_replacement = """6.3  测试用例
　　针对系统核心的文生图、文生视频、图生视频、图像拓展以及智能对话五大多模态AIGC创作功能，本研究设计了多组输入数据与边界值用例以验证功能的正确性与越权安全防御能力。具体测试用例如下：
　　（1）文生图功能测试：测试涵盖提示词为空拦截、正常提示词与参数返回任务ID、尺寸参数非法校验拦截、随机种子越界校验拦截以及生成数量上限校验拦截。
表5  文生图功能测试用例表
　　（2）文生视频功能测试：包括空描述拦截、合规参数的异步创建与轮询校验、非法分辨率拦截、随机种子越界拦截以及手机竖屏等多种长宽比分辨率的通过性验证。
表6  文生视频功能测试用例表
　　（3）图生视频功能测试：验证未上传图片时的校验拦截、单图输入模式、首尾帧图片输入模式下的正常处理逻辑、视频时长超出范围的拦截以及非法图片地址的校验。
表7  图生视频功能测试用例表
　　（4）图像拓展功能测试：包括缺少主体图片ID时的拦截、合法拓展比例与偏置、拓展倍率超出范围（如大于3倍）的拦截校验、空参数拦截以及高画质拓展模式测试。
表8  图像拓展功能测试用例表
　　（5）智能对话功能测试：测试发送空消息拦截、未指定模型时的默认适配、单次发送超长文本的拦截、非法大模型标识的拦截以及未登录用户访问受限接口的防越权机制。
表9  智能对话功能测试用例表

"""
        content_norm = content_norm[:ch63_start] + ch63_replacement + content_norm[ch64_start:]
        print("Chapter 6.3 test cases tables replaced successfully!")
    else:
        print("Error: Chapter 6.3 or 6.4 boundaries not found")

    # 4. Chapter 7 replacement (Step 621 version)
    ch7_start = content_norm.find("7  总结与展望")
    refs_start = content_norm.find("参  考  文  献")
    if ch7_start != -1 and refs_start != -1:
        ch7_replacement = """7  总结与展望

　　本研究为了解决多模态AIGC内容激增引起的资产治理与协同信任危机，设计并开发了一套基于Spring Boot与Vue 3的多模态AI图库系统。系统将生成与治理一体化作为核心理念，通过轻量级Sa-Token实现接口级细粒度安全防御，并依托腾讯云COS与数据万象实现对象存储与违规内容审计。同时，为了满足创作者移动端即时创作与设备协同的应用诉求，项目同步研发了基于uni-app的跨端移动应用（如pixelhub-uni-app-dev），完成了针对移动终端的适配与多端编译，实现了移动端资产预览、智能创作与协同空间的敏捷管理，满足了多终端无缝流转的工程要求。高并发压测表明，系统整体性能强健，响应迅速，具备良好的工程实用价值。
　　未来，系统将从检索语义化与数据持久化方向进行升级。第一，引入CLIP双塔模型与Milvus向量数据库，提升图像高维语义特征的精准匹配与相似度检索能力；第二，将高并发审计日志与历史分析数据迁移至分布式非关系型时序存储中，以确保在大规模商用场景下系统的吞吐性能。

"""
        content_norm = content_norm[:ch7_start] + ch7_replacement + content_norm[refs_start:]
        print("Chapter 7 replaced successfully!")
    else:
        print("Error: Chapter 7 or References boundaries not found")

    # Save to disk with proper encoding and line endings
    with open(path_txt, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(content_norm)
    print("Successfully wrote ultimate modifications to 稿件-v4.txt!")

if __name__ == "__main__":
    main()
