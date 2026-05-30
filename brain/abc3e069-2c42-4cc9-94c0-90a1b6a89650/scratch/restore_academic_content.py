import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Replace Chapter 2
    ch2_target = """2  相关技术介绍

2.1  Spring Boot框架
　　Spring Boot是基于Spring框架的快速开发脚手架，核心理念是约定优于配置，通过自动装配机制最大程度简化了繁琐的XML配置[9]。系统基于Spring Boot 2.7.6版本，利用内置Tomcat容器实现服务的独立部署，通过Spring MVC组件提供RESTful API接口。

2.2  Vue.js框架
　　Vue.js是用于构建用户界面的渐进式JavaScript框架，Vue 3的高效虚拟DOM和Diff算法极大优化了渲染性能[10]。项目选用Vue 3并引入组合式API，使业务逻辑高度聚合，提升了前端代码的可维护性与复用性。

2.3  MyBatis-Plus持久层框架
　　MyBatis-Plus是MyBatis的增强工具，在保留原特性的基础上引入了ActiveRecord模式与强大的CRUD接口。系统利用其条件构造器实现复杂检索，并通过内置分页插件实现高效的服务端物理分页。

2.4  Redis与Caffeine二级缓存
　　为应对高并发读取场景，系统构建了包含Caffeine本地缓存和Redis分布式缓存的多级缓存体系，分别用于缓存本地热点数据与Session会话、分布式锁。当请求到来时，系统先查询Caffeine，未命中则查询Redis，最后回源数据库，大幅降低了IO延迟与数据库负载。

2.5  Sa-Token安全框架
　　系统选用轻量级权限认证框架Sa-Token实现安全管控。在会话管理上，结合Cookie与Session机制，登录后Token存于客户端，服务端维护Session。配合Sa-Token的注解鉴权，实现对接口的细粒度控制，构建了严密的RBAC权限模型。

2.6  腾讯云COS与数据万象
　　系统采用腾讯云对象存储COS实现海量文件分布式存储，并与数据万象CI服务深度整合。文件采用前端直传模式，由数据万象服务在云端自动完成图片压缩、缩略图生成、Exif元数据解析与违规内容审核，降低了带宽负载与运营风险。

2.7  WebSocket协议
　　在团队空间协同编辑模块中，系统采用WebSocket长连接通信协议。WebSocket用于实时同步多名成员的操作指令与编辑锁状态，有效避免了多人同时修改同一图片的并发冲突。

2.8  MySQL数据库
　　项目选用MySQL 5.7版本作为核心关系型数据库，利用InnoDB引擎的ACID事务特性保障业务数据的完整性，并使用JSON原生类型存储多维分类与标签数据。

2.9  Apache ECharts图表库
　　系统在空间分析模块中引入开源可视化图表库Apache ECharts，通过饼图、折线图、词云图等形式构建数据驾驶舱，直观展示空间存储分布、上传趋势与内容主题。"""

    ch2_replacement = """2  相关技术介绍

　　本系统采用标准的前后端分离架构，基于后端Spring Boot与前端Vue 3核心框架搭建。为满足高并发热点读取、协同编辑、多模态AIGC对接与云端海量资源管理的工程需求，系统在持久层选用MyBatis-Plus持久层框架简化CRUD开发，使用MySQL 5.7作为核心关系型数据库，并引入Redis与Caffeine构建二级缓存体系以提升热点数据检索性能。安全管控层选用轻量级权限认证框架Sa-Token构建细粒度的RBAC角色权限模型。海量文件分布式存储与智能处理依托腾讯云COS与数据万象服务实现前端直传及智能处理，跨终端协同编辑通过WebSocket协议实时同步编辑锁状态。此外，系统通过开源可视化图表库Apache ECharts构建数据驾驶舱，并深度对接阿里云百炼大模型平台API实现多模态AIGC核心任务的异步分发与状态机收敛。

2.1  Spring Boot框架
　　Spring Boot是基于Spring框架的快速开发脚手架，核心理念是约定优于配置，通过自动装配机制最大程度简化了繁琐的XML配置[9]。系统基于Spring Boot 2.7.6版本，利用内置Tomcat容器实现服务的独立部署，通过Spring MVC组件提供RESTful API接口。

2.2  Vue.js框架
　　Vue.js是用于构建用户界面的渐进式JavaScript框架，Vue 3的高效虚拟DOM和Diff算法极大优化了渲染性能[10]。项目选用Vue 3并引入组合式API，使业务逻辑高度聚合，提升了前端代码的可维护性与复用性。"""

    if ch2_target in content:
        content = content.replace(ch2_target, ch2_replacement)
        print("Chapter 2 consolidated successfully!")
    else:
        # Let's try replacement with different carriage returns if necessary
        normalized_content = content.replace("\r\n", "\n")
        normalized_target = ch2_target.replace("\r\n", "\n")
        normalized_replacement = ch2_replacement.replace("\r\n", "\n")
        if normalized_target in normalized_content:
            normalized_content = normalized_content.replace(normalized_target, normalized_replacement)
            content = normalized_content
            print("Chapter 2 consolidated with CR/LF normalized!")
        else:
            print("Error: Could not find Chapter 2 target exactly")

    # 2. Replace Chapter 3.1 Technical Feasibility
    feasibility_target = "技术可行性：采用成熟的前后端分离体系（Spring Boot + Vue 3），并引入Redis+Caffeine二级缓存、WebSocket长连接实时同步和事务控制，具有良好的健壮性与可复用性。"
    feasibility_replacement = "技术可行性：采用成熟的Spring Boot与Vue 3前后端分离体系，并引入Redis与Caffeine二级缓存、WebSocket长连接实时同步和事务控制，具有良好的健壮性与可复用性。"
    if feasibility_target in content:
        content = content.replace(feasibility_target, feasibility_replacement)
        print("Chapter 3.1 technical feasibility updated successfully!")
    else:
        print("Error: Could not find technical feasibility sentence exactly")

    # 3. Replace Chapter 7
    ch7_target = """7  总结与展望

7.1  本文主要工作成果
　　本文为了解决多模态AIGC内容大量增加所引起的治理困难，开发了基于Spring Boot与Vue 3的多模态AI图库系统。主要成果有：第一，基于MySQL、Redis、Caffeine和腾讯云COS搭建了高性能全栈技术底座；第二，实现了文生图、文生视频、图生视频、图像拓展与智能对话五大AIGC核心功能，利用接口隔离封装大模型API；第三，设计了私有与团队空间配额管理和细粒度RBAC鉴权；第四，采用WebSocket协同编辑锁与数据万象元数据解析优化协同体验；第五，系统通过了高并发压力测试，具有实用工程价值。

7.2  未来展望与改进方向
　　系统目前主要支持图片和视频模态，后续计划增加音频大模型接入。其次，检索方式仍基于标签 and 分类，未来计划引入CLIP双塔模型，在向量数据库Milvus中进行图像的高维语义特征向量检索。再次，系统的审计日志目前存储在MySQL中，在高并发场景下存在瓶颈，未来将迁移至更符合时序特性的存储媒介中，使系统更加安全稳健。"""

    ch7_replacement = """7  总结与展望

　　本文针对多模态AIGC内容快速增长所带来的治理与存储难题，设计并实现了一套基于Spring Boot与Vue 3的多模态AI图库系统。通过结合MySQL关系型存储、Redis与Caffeine二级缓存以及腾讯云COS对象存储，系统成功搭建了高性能、安全可控的全栈技术底座。系统不仅实现了文生图、文生视频、图生视频、图像拓展与智能对话五大核心AIGC功能的异步创建与状态机生命周期收敛，还设计了基于命名空间配额的私有与团队空间细粒度权限控制体系。利用数据万象元数据解析、WebSocket协同编辑锁与多维可视化分析，显著优化了资产协同与管理体验。高并发压力测试与资源监控表明，系统在核心API吞吐与平均延迟响应上表现优异，具备极高的稳定性和实用工程价值。
　　未来，系统将从跨终端协同、语义检索与弹性存储三个方向进行演进。第一，跨终端协同生态构建。针对创作者移动化即时创作与多设备无缝流转的工程诉求，后续计划深入适配基于Vue.js的跨端统一开发框架uni-app，针对已研发的移动端应用实施多端编译与打包部署，实现Web端与移动终端的跨屏无缝资产协同。第二，检索智能化升级。未来计划引入CLIP双塔模型与Milvus向量数据库，以提升图像的多维语义检索能力。第三，数据存储的弹性伸缩。将高并发审计日志与海量元数据迁移至更符合时序特性的分布式非关系型数据库中，使系统在大规模商用场景下更加稳健高效。"""

    if ch7_target in content:
        content = content.replace(ch7_target, ch7_replacement)
        print("Chapter 7 consolidated successfully!")
    else:
        normalized_content = content.replace("\r\n", "\n")
        normalized_target = ch7_target.replace("\r\n", "\n")
        normalized_replacement = ch7_replacement.replace("\r\n", "\n")
        if normalized_target in normalized_content:
            normalized_content = normalized_content.replace(normalized_target, normalized_replacement)
            content = normalized_content
            print("Chapter 7 consolidated with CR/LF normalized!")
        else:
            print("Error: Could not find Chapter 7 target exactly")

    with open(path_txt, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("稿件-v4.txt updated successfully!")

if __name__ == "__main__":
    main()
