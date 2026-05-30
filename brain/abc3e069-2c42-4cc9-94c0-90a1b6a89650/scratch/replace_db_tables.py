import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("Text file not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_block = """4.3.2  逻辑结构设计
　　系统采用MySQL作为关系型数据库。为了实现对多用户、多命名空间以及多模态图片资产的精细化治理，数据库设计了四个核心实体表，其表名与描述如下所示：
　　（1）用户表（user）：用户表主要存储平台用户的账号、加盐密码、昵称、头像、平台角色以及审计时间等，具体的表结构设计如表1所示。
表1  用户表（user）
　　（2）图片表（picture）：图片表主要记录多模态图像的存储路径、名称、分类与JSON标签、图片尺寸像素、文件大小以及所属空间和人工审核状态，具体的表结构设计如表2所示。
表2  图片表（picture）
　　（3）空间表（space）：设计了最大容量和最大数量字段，以支持个人私有空间与多租户团队空间的存储配额限额控制，具体的表结构设计如表3所示。
表3  空间表（space）
　　（4）空间成员表（space_user）：保存用户与空间的映射关系，记录用户在特定空间中的角色（管理员、编辑者、浏览者），用以支持Sa-Token的细粒度RBAC鉴权，具体的表结构设计如表4所示。
表4  空间成员表（space_user）"""

    new_block = """4.3.2  逻辑结构设计
　　系统采用MySQL作为关系型数据库。为了实现对多用户、多命名空间以及多模态图片资产的精细化治理，数据库设计了四个核心实体表，分别为用户表（user）、图片表（picture）、空间表（space）以及空间成员关联表（space_user）。通过对用户凭证加盐加密存储、空间成员角色控制、对象直传元数据管理等字段的设计，以及合理设置主外键与高频查询索引，在保证数据存储安全性的同时，有效支撑了系统各业务模块的高效协同与稳定运行。
　　为进一步提升系统在未来多模态业务延伸中的高扩展性，系统底层数据模型预留了清晰的演进与拓充空间。未来可通过引入视频资源表（video）来扩展对短视频与动态多媒体资产的属性表征（如帧率、编码格式、时段跨度等）；引入模型配置表（model_config）用以支持多维度文生图、图生图大模型API的动态计费权重与动态路由配置；同时，通过拓充AIGC异步任务表（aigc_task）实现对耗时较长的视频生成、多模态解析等任务的生命周期状态追踪（排队中、执行中、已完成、执行失败）与回调鉴权。这一极具前瞻性的数据库模型设计，不仅论证了系统架构在多模态AI演进中的韧性，也为系统向全场景多模态资产治理平台的迭代奠定了坚实的数据底座。"""

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(path_txt, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully updated database section in 稿件-v4.txt!")
    else:
        # Fallback check if space or character variants exist
        print("Exact block match not found, looking for partial match...")
        # We can do a line-by-line replacement or regex replacement to be 100% robust!
        lines = content.splitlines()
        start_idx = -1
        end_idx = -1
        for idx, l in enumerate(lines):
            if "4.3.2  逻辑结构设计" in l or "4.3.2 逻辑结构设计" in l:
                start_idx = idx
            if start_idx != -1 and "表4  空间成员表" in l:
                end_idx = idx
                break
        if start_idx != -1 and end_idx != -1:
            new_lines = lines[:start_idx + 1] + [
                "　　系统采用MySQL作为关系型数据库。为了实现对多用户、多命名空间以及多模态图片资产的精细化治理，数据库设计了四个核心实体表，分别为用户表（user）、图片表（picture）、空间表（space）以及空间成员关联表（space_user）。通过对用户凭证加盐加密存储、空间成员角色控制、对象直传元数据管理等字段的设计，以及合理设置主外键与高频查询索引，在保证数据存储安全性的同时，有效支撑了系统各业务模块的高效协同与稳定运行。",
                "　　为进一步提升系统在未来多模态业务延伸中的高扩展性，系统底层数据模型预留了清晰的演进与拓充空间。未来可通过引入视频资源表（video）来扩展对短视频与动态多媒体资产的属性表征（如帧率、编码格式、时段跨度等）；引入模型配置表（model_config）用以支持多维度文生图、图生图大模型API的动态计费权重与动态路由配置；同时，通过拓充AIGC异步任务表（aigc_task）实现对耗时较长的视频生成、多模态解析等任务的生命周期状态追踪（排队中、执行中、已完成、执行失败）与回调鉴权。这一极具前瞻性的数据库模型设计，不仅论证了系统架构在多模态AI演进中的韧性，也为系统向全场景多模态资产治理平台的迭代奠定了坚实的数据底座。"
            ] + lines[end_idx + 1:]
            with open(path_txt, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            print("Successfully updated database section using line-based replacement!")
        else:
            print("Failed to find logical database section boundaries")

if __name__ == "__main__":
    main()
