import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("Text file not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Locate 6.3 and replace with the ultra-condensed version of the 5 paragraphs
    lines = content.splitlines()
    start_idx = -1
    end_idx = -1
    for idx, l in enumerate(lines):
        if "6.3  " in l or "6.3 " in l:
            start_idx = idx
        if start_idx != -1 and ("6.4  测试结论" in l or "6.4 测试结论" in l):
            end_idx = idx
            break
            
    if start_idx != -1 and end_idx != -1:
        new_lines = lines[:start_idx] + [
            "6.3  系统功能测试与边界校验",
            "　　本研究针对系统核心的文生图、文生视频、图生视频、图像拓展与智能对话五大多模态AIGC创作功能开展黑盒边界测试与防越权安全校验。为精炼篇幅，具体测试过程与核心校验逻辑阐述如下：",
            "　　在文生图功能测试中，系统基于Sa-Token的PICTURE_EDIT权限实行拦截，并对prompt字符数（<=800）、生成数量n（1至4）、随机种子seed（0至2147483647）以及图片分辨率格式进行边界校验。服务层以5秒为周期轮询生成状态，在SUCCEEDED后自动归档至用户空间并记录审计与配额日志。经验证合法与异常参数等组合场景均精准通过。",
            "　　在文生视频功能测试中，系统对prompt进行字符清理并限制在800字内，分辨率size仅限1280*720等标准枚举，时长固定为5秒。控制器异步创建任务并返回初始PENDING/RUNNING状态的taskId，并在轮询完成后演进至SUCCEEDED以提供播放下载。越界种子与非法分辨率等异常用例均被成功拦截。",
            "　　在图生视频功能测试中，系统严格校验单图输入（提供imageUrl）与首尾帧输入模式（提供first/lastFrameUrl）的互斥性。系统限制分辨率支持480P与720P，视频时长在3至5秒之间，随机种子介于0至2147483647。测试用例证实未传图片拦截、时长越界及非法地址校验等逻辑均完全符合预期。",
            "　　在图像拓展功能测试中，执行用户须持PICTURE_EDIT权限，系统校验外延比例x与yScale（1.0至3.0）以及像素偏移（0至10000）的边界范围，并支持最佳画质模式与尺寸控制。服务层将扩图成功后的结果写回COS临时存储供用户确认。测试用例涵盖倍数越界与空偏移量拦截，防御逻辑完备无缺。",
            "　　在智能对话功能测试中，接口层要求messages非空且model留空自动回退至默认大模型。系统创建任务后将PROCESSING状态写入Redis并设10分钟有效期，支持前端以每次5秒、最多60次的频率轮询检索最终结果。经测试空消息、消息超长与未登录越权访问等场景均被精准拦截。",
            ""
        ] + lines[end_idx:]
        with open(path_txt, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print("Successfully condensed 6.3 paragraphs in 稿件-v4.txt!")
    else:
        print("Failed to find heading indices")

if __name__ == "__main__":
    main()
