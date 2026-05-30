import os

def get_table_0_to_3():
    # Constructing Table 1 to Table 4 based on 大论文原文.md and extracted_tables.txt
    table_1 = """表1  用户表（user）
| 字段名 | 数据类型 | 长度 | 是否为空 | 是否主键 | 描述 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| id | bigint | 20 | 否 | 是 | 唯一标识符 |
| userAccount | varchar | 256 | 否 | 否 | 用户账号 |
| userPassword | varchar | 512 | 否 | 否 | 加盐密码 |
| userName | varchar | 256 | 是 | 否 | 用户昵称 |
| userAvatar | varchar | 1024 | 是 | 否 | 头像地址 |
| userProfile | varchar | 512 | 是 | 否 | 用户简介 |
| userRole | varchar | 256 | 否 | 否 | 平台角色 |
| editTime | datetime | - | 否 | 否 | 编辑时间 |
| createTime | datetime | - | 否 | 否 | 创建时间 |
| updateTime | datetime | - | 否 | 否 | 更新时间 |
| isDelete | tinyint | 4 | 否 | 否 | 逻辑删除 |
| vipExpireTime | datetime | - | 是 | 否 | 会员过期时间 |
| vipCode | varchar | 128 | 是 | 否 | 兑换码 |
| vipNumber | bigint | 20 | 是 | 否 | 会员号 |"""

    table_2 = """表2  图片表（picture）
| 字段名 | 数据类型 | 长度 | 是否为空 | 是否主键 | 描述 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| id | bigint | 20 | 否 | 是 | 唯一标识符 |
| url | varchar | 512 | 否 | 否 | 图片地址 |
| name | varchar | 128 | 否 | 否 | 图片名称 |
| introduction | varchar | 512 | 是 | 否 | 图片简介 |
| category | varchar | 64 | 是 | 否 | 图片分类 |
| tags | varchar | 512 | 是 | 否 | JSON标签 |
| picSize | bigint | 20 | 是 | 否 | 文件大小 |
| picWidth | int | 11 | 是 | 否 | 像素宽度 |
| picHeight | int | 11 | 是 | 否 | 像素高度 |
| picScale | double | - | 是 | 否 | 宽高比 |
| picFormat | varchar | 32 | 是 | 否 | 图片格式 |
| userId | bigint | 20 | 否 | 否 | 创建用户ID |
| spaceId | bigint | 20 | 是 | 否 | 所属空间ID |
| thumbnailUrl | varchar | 512 | 是 | 否 | 缩略图地址 |
| picColor | varchar | 16 | 是 | 否 | 主色调 |
| reviewStatus | int | 11 | 否 | 否 | 审核状态(0-待审核, 1-通过, 2-拒绝) |
| reviewMessage | varchar | 512 | 是 | 否 | 审核信息 |
| reviewerId | bigint | 20 | 是 | 否 | 审核人ID |
| reviewTime | datetime | - | 是 | 否 | 审核时间 |
| createTime | datetime | - | 否 | 否 | 创建时间 |
| editTime | datetime | - | 否 | 否 | 编辑时间 |
| updateTime | datetime | - | 否 | 否 | 更新时间 |
| isDelete | tinyint | 4 | 否 | 否 | 逻辑删除 |"""

    table_3 = """表3  空间表（space）
| 字段名 | 数据类型 | 长度 | 是否为空 | 是否主键 | 描述 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| id | bigint | 20 | 否 | 是 | 唯一标识符 |
| spaceName | varchar | 128 | 是 | 否 | 空间名称 |
| spaceLevel | int | 11 | 是 | 否 | 空间级别配额 |
| spaceType | int | 11 | 否 | 否 | 空间类型(0-私有, 1-团队) |
| maxSize | bigint | 20 | 是 | 否 | 最大容量 |
| maxCount | bigint | 20 | 是 | 否 | 最大数量 |
| totalSize | bigint | 20 | 是 | 否 | 当前已用容量 |
| totalCount | bigint | 20 | 是 | 否 | 当前已存数量 |
| userId | bigint | 20 | 否 | 否 | 所属用户ID |
| createTime | datetime | - | 否 | 否 | 创建时间 |
| editTime | datetime | - | 否 | 否 | 编辑时间 |
| updateTime | datetime | - | 否 | 否 | 更新时间 |
| isDelete | tinyint | 4 | 否 | 否 | 逻辑删除 |"""

    table_4 = """表4  空间成员表（space_user）
| 字段名 | 数据类型 | 长度 | 是否为空 | 是否主键 | 描述 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| id | bigint | 20 | 否 | 是 | 唯一标识符 |
| spaceId | bigint | 20 | 否 | 否 | 空间ID |
| userId | bigint | 20 | 否 | 否 | 用户ID |
| spaceRole | varchar | 128 | 是 | 否 | 空间角色(admin/editor/viewer) |
| createTime | datetime | - | 否 | 否 | 创建时间 |
| updateTime | datetime | - | 否 | 否 | 更新时间 |"""

    return "\\n\\n".join([table_1, table_2, table_3, table_4])


def get_table_4_to_8():
    # Constructing Table 5 to Table 9
    table_5 = """表5  文生图功能测试用例表
| 序号 | 操作 | 输入数据 | 预期结果 | 结果 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 不输入数据，点击创建任务 | prompt=null、size=null、promptExtend=true、n=1 | 提示输入不能为空 | 通过 |
| 2 | 输入正确提示词与合法参数 | prompt=湖面微波荡漾，远山雪线映天际，晨雾与金色阳光交织，岸边松林随风起伏，整体清亮写意、size=9:16（手机竖屏）、promptExtend=true、n=3 | 返回任务ID；状态 SUCCEEDED；提供图片URL列表 | 通过 |
| 3 | 输入非法尺寸参数 | prompt=山谷清晨薄雾，淡粉天际渐亮，静水如镜，远处木屋与松林点缀、size=1000xABC、promptExtend=false、n=1 | 参数校验失败；返回错误码 | 通过 |
| 4 | 随机种子越界 | prompt=湿漉街道倒映霓虹，未来感机器人巡游，红紫蓝灯交错，高对比度清晰主体、size=16:9（宽屏）、promptExtend=true、n=1、seed=2147483648 | 参数校验失败；返回错误码 | 通过 |
| 5 | 生成数量越界 | prompt=悬浮车穿梭的高架通道，玻璃幕墙反射天空与霓虹，远处巨型广告牌闪烁，冷色科幻风、size=1:1（方形）、promptExtend=true、n=5 | 参数校验失败；返回错误码 | 通过 |"""

    table_6 = """表6  文生视频功能测试用例表
| 序号 | 操作 | 输入数据 | 预期结果 | 结果 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 不输入提示词，点击创建任务 | prompt=null、size=null、promptExtend=true、seed=123 | 提示输入不能为空 | 通过 |
| 2 | 输入合法提示词与参数 | prompt=湿润巷道在雨夜中泛光，霓虹灯牌映照水面，远处车灯拖出光轨，镜头低角度强调空间纵深、size=1280*720、promptExtend=true、seed=1234 | 返回任务ID；状态 PENDING 或 RUNNING | 通过 |
| 3 | 输入非法分辨率 | prompt=晨雾弥漫的山谷，微风拂过草甸，远处木栈道隐现，柔和清新自然风格、size=1234*567、promptExtend=false、seed=5678 | 参数校验失败；返回错误码 | 通过 |
| 4 | 随机种子越界 | prompt=长焦拍摄的城市大道，雨幕中霓虹与车灯交织，色彩高饱和、影调对比鲜明、size=1280*720、promptExtend=true、seed=2147483648 | 参数校验失败；返回错误码 | 通过 |
| 5 | 合法参数：纵版分辨率 | prompt=窄巷深处的霓虹雨夜，人物在光影中剪影前行，地面水洼形成镜面反射，电影质感、size=720*1280、promptExtend=true、seed=5678 | 返回任务ID；状态 PENDING 或 RUNNING | 通过 |"""

    table_7 = """表7  图生视频功能测试用例表
| 序号 | 操作 | 输入数据 | 预期结果 | 结果 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 未选择图片创建任务 | prompt=null、resolution=720P、duration=5、seed=1234、promptExtend=true、imageUrl=null | 提示输入不能为空 | 通过 |
| 2 | 单图模式：设置合法参数 | prompt=荒野夕阳下的女骑士拔剑，与远处巨龙对峙；暖橙与深蓝对比，低角度、电影级构图、resolution=720P、duration=5、seed=931164829、promptExtend=true、imageUrl=url | 返回任务ID；状态 PENDING 或 RUNNING | 通过 |
| 3 | 首尾帧模式：提供首尾帧 | prompt=暮色之下女骑士从静到动的镜头推进；首帧为静态准备，尾帧为决绝前行，镜头语言连贯、resolution=720P、duration=5、seed=931164829、promptExtend=true、firstFrameUrl=url1、lastFrameUrl=url2 | 返回任务ID；状态 PENDING 或 RUNNING | 通过 |
| 4 | 时长越界 | prompt=荒野夕阳下的女骑士拔剑，与远处巨龙对峙；暖橙与深蓝对比、resolution=720P、duration=2、seed=1234、promptExtend=true、imageUrl=url | 参数校验失败；返回错误码 | 通过 |
| 5 | 图片 URL 非法 | prompt=女骑士跃上断桥的瞬间，风卷起披风与尘土，强叙事、动态倾向、resolution=720P、duration=5、seed=1234、promptExtend=true、imageUrl=not-a-url | 参数校验失败；返回错误码 | 通过 |"""

    table_8 = """表8  图像拓展功能测试用例表
| 序号 | 操作 | 输入数据 | 预期结果 | 结果 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 缺少图片ID | pictureId=null、mode=ratio_expand、quality=normal、limitImageSize=true、scale=2.0 | 提示图片ID不能为空 | 通过 |
| 2 | 设置合法参数 | pictureId=1996139001012625410、mode=ratio_expand、quality=normal、limitImageSize=true、scale=2.0 | 返回任务ID；状态 PENDING 或 RUNNING | 通过 |
| 3 | 倍数越界 | pictureId=1996139003705368577、mode=ratio_expand、quality=normal、limitImageSize=true、scale=3.5 | 参数校验失败；返回错误码 | 通过 |
| 4 | 未设置比例或偏移量 | pictureId=1996139005919961090、mode=pixel_offset、offsets=null、xScale=null、yScale=null | 参数校验失败 | 通过 |
| 5 | 开启最佳质量 | pictureId=1996139007715123202、mode=ratio_expand、quality=best、limitImageSize=true、scale=2.5 | 返回任务ID；状态 PENDING 或 RUNNING | 通过 |"""

    table_9 = """表9  智能对话功能测试用例表
| 序号 | 操作 | 输入数据 | 预期结果 | 结果 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 发送空消息 | messages=null | 提示输入不能为空 | 通过 |
| 2 | 模型留空发送消息 | model=null、messages=[{role=user, content=请根据以下场景生成三条检索短语...}] | 返回 taskId；状态 PROCESSING | 通过 |
| 3 | 消息过长超限 | messages=[{role=user, content=在黄昏海港的长镜头叙事中...}] | 参数校验失败；返回错误码 | 通过 |
| 4 | 模型非法不在白名单 | model=unknown_model、messages=[{role=user, content=请为“雨夜巷道的霓虹反射”...}] | 参数校验失败；返回错误码 | 通过 |
| 5 | 未登录访问 | token=null、messages=[{role=user, content=请输出关于“旧城街区的霓虹与湿地反射”...}] | 返回未授权 | 通过 |"""

    return "\\n\\n".join([table_5, table_6, table_7, table_8, table_9])

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace Table 1-4 block
    # Start of Table 1 block: "表1  用户表（user）"
    # End of Table 4 block: is right before "\n\n5  系统实现" or "5  系统实现"
    t1_idx = content.find("表1  用户表（user）")
    sys_impl_idx = content.find("5  系统实现")
    
    if t1_idx != -1 and sys_impl_idx != -1:
        prefix = content[:t1_idx]
        suffix = content[sys_impl_idx:]
        tables_0_3 = get_table_0_to_3().replace("\\n", "\n")
        # Keep double-byte indentations for sections, but tables shouldn't have indentations
        new_content = prefix + tables_0_3 + "\n\n\n" + suffix
        content = new_content
        print("Table 1-4 replaced successfully")
    else:
        print(f"Error: Table 1 start={t1_idx}, sys_impl={sys_impl_idx}")
        
    # Replace Table 5-9 block
    # Start of Table 5 block: "表5  文生图功能测试用例表"
    # End of Table 9 block: is right before "\n\n6.4  测试结论" or "6.4  测试结论"
    t5_idx = content.find("表5  文生图功能测试用例表")
    sys_conclusion_idx = content.find("6.4  测试结论")
    
    if t5_idx != -1 and sys_conclusion_idx != -1:
        prefix = content[:t5_idx]
        suffix = content[sys_conclusion_idx:]
        tables_4_8 = get_table_4_to_8().replace("\\n", "\n")
        new_content = prefix + tables_4_8 + "\n\n" + suffix
        content = new_content
        print("Table 5-9 replaced successfully")
    else:
        print(f"Error: Table 5 start={t5_idx}, sys_conclusion={sys_conclusion_idx}")
        
    with open(path_txt, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("稿件-v4.txt updated successfully!")

if __name__ == "__main__":
    main()
