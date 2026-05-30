import os

def main():
    path_v3 = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v3.txt"
    path_v4 = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    
    with open(path_v3, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Let's perform replacements in the text
    # 1 Introduction citations
    content = content.replace("生成式大模型技术降低了多媒体内容的生产门槛。", "生成式大模型技术降低了多媒体内容的生产门槛[1]。")
    content = content.replace("采样器Sampler等高维参数。", "采样器Sampler等高维参数[1]。")
    content = content.replace("致使创作过程无法回溯。", "致使创作过程无法回溯[2]。")
    content = content.replace("多模态AI图库系统，为AI时代的", "多模态AI图库系统[2]，为AI时代的")
    
    # 1.1 background citations
    content = content.replace("AIGC已成为行业关注重点。", "AIGC已成为行业关注重点[1]。")
    content = content.replace("容易产生覆盖误操作。", "容易产生覆盖误操作[3]。")
    content = content.replace("实现高效存储与合规审计。", "实现高效存储与合规审计[4]。")
    content = content.replace("为同类垂直AI应用的研发提供了参考。", "为同类垂直AI应用的研发提供了参考[4]。")
    
    # 1.2 status citations
    content = content.replace("国外在AIGC技术与应用层面起步较早。", "国外在AIGC技术与应用层面起步较早[5]。")
    content = content.replace("缺乏多用户管理与云端协同机制。", "缺乏多用户管理与云端协同机制[6]。")
    content = content.replace("商业准入与管理规范，", "商业准入与管理规范[7]，")
    content = content.replace("国内AIGC领域近年来呈现快速追赶与爆发态势。", "国内AIGC领域近年来呈现快速追赶与爆发态势[8]。")
    
    # Chapter 2 citations
    content = content.replace("集成了阿里云百炼大模型平台、", "集成了阿里云百炼大模型平台[8]、")
    content = content.replace("最大程度简化了繁琐的XML配置。", "最大程度简化了繁琐的XML配置[9]。")
    content = content.replace("极大优化了渲染性能。", "极大优化了渲染性能[10]。")
    
    # Update Bibliography
    # Let's search for "参  考  文  献"
    ref_idx = content.find("参  考  文  献")
    ack_idx = content.find("致        谢")
    
    if ref_idx != -1 and ack_idx != -1:
        new_refs = """参  考  文  献

[1]  Cao Y, Li S, Liu Y, et al. A Survey of AI-Generated Content (AIGC) [J]. ACM Computing Surveys, 2025, 57(5): 1–38.
[2]  刘明亮.人工智能生成内容(AIGC)技术特征及应用场景分析[J].信息记录材料,2023,24(10):234-236.DOI:10.16009/j.cnki.cn13-1295/tq.2023.10.010.
[3]  Wang Z, Shen L, Kuang E, et al. Exploring the Impact of Artificial Intelligence-Generated Content (AIGC) Tools on Social Dynamics in UX Collaboration [C]. Designing Interactive Systems Conference, 2024: 1594–1606.
[4]  吴凡,毛祖光,刘华.AIGC技术在视觉传达设计行业中的影响与发展策略探究[J].阜阳师范大学学报(社会科学版),2024,(03):147-156.DOI:10.14096/j.cnki.cn34-1333/c.2024.03.22.
[5]  Xu Y. Evolution and future directions of Artificial Intelligence Generated Content (AIGC): A comprehensive review [J]. Applied and Computational Engineering, 2024, 95(1): 1–13.
[6]  徐厚岩.人工智能生成内容的技术体系与应用场景分析[J].电视技术,2024,48(04):149-151.DOI:10.16280/j.videoe.2024.04.040.
[7]  Brilli S, Gemini L, Spaggiari C. GENERIC WAR IMAGINARIES: AI-GENERATED IMAGES OF THE ISRAEL-GAZA CONFLICT IN THE ADOBE STOCK CONTROVERSY [J]. AoIR Selected Papers of Internet Research, 2025.
[8]  阿里云计算有限公司. 阿里云百炼: 一站式大模型应用开发平台[EB/OL]. (2023-10-31)[2025-12-12]. https://bailian.console.aliyun.com/?tab=doc#/doc/?type=model&url=2579562.
[9]  王志亮,纪松波.基于SpringBoot的Web前端与数据库的接口设计[J].工业控制计算机,2023,36(03):51-53.
[10] 夏祎忞.Vue.js框架下Web前端组件化开发模式实践分析[J].信息与电脑,2025,37(22):125-127.

"""
        content = content[:ref_idx] + new_refs + content[ack_idx:]
        print("Successfully updated bibliography in draft!")
    else:
        print(f"Failed to find ref_idx ({ref_idx}) or ack_idx ({ack_idx})")
        
    with open(path_v4, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully processed and wrote v4 manuscript to {path_v4}")

if __name__ == "__main__":
    main()
