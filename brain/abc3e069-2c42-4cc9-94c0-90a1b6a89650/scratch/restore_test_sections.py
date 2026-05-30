import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("Text file not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We will locate 6.3 and replace the compressed block back to the 5 distinct sub-sections!
    lines = content.splitlines()
    start_idx = -1
    end_idx = -1
    for idx, l in enumerate(lines):
        if "6.3  测试用例与核心逻辑" in l or "6.3  测试用例" in l or "6.3 测试用例" in l:
            start_idx = idx
        if start_idx != -1 and ("6.4  测试结论" in l or "6.4 测试结论" in l):
            end_idx = idx
            break
            
    if start_idx != -1 and end_idx != -1:
        new_lines = lines[:start_idx] + [
            "6.3  测试用例与校验逻辑",
            "　　针对系统核心的文生图、文生视频、图生视频、图像拓展以及智能对话五大多模态AIGC创作功能，本研究设计了多组输入数据与边界值用例以验证功能的正确性与越权安全防御能力。由于篇幅有限，本稿件对具体的表格型测试用例进行精简与提炼，以学术自然段方式对各模块的测试过程与核心校验逻辑阐述如下：",
            "",
            "　　6.3.1  文生图功能测试",
            "　　文生图功能测试重点进行权限和参数的校验，并覆盖任务创建、状态轮询与结果入库的完整生命周期。在空间维度上，系统基于Sa-Token的PICTURE_EDIT权限实行拦截；在参数校验上，限制prompt提示词不超过800字符、生成数量n介于1至4之间、随机种子seed范围为0至2147483647，并对图片分辨率格式进行严格匹配。服务层以5秒为周期轮询生成状态，当状态收敛为SUCCEEDED时自动归档至用户空间，并同步扣减存储配额与记录审计日志。测试用例涵盖了参数空白、合法参数返回任务ID、尺寸参数非法、种子与数量越界等多种异常与越权组合场景，经验证所有测试项均精准拦截并成功通过。",
            "",
            "　　6.3.2  文生视频功能测试",
            "　　文生视频功能测试重点校验文本提示、分辨率枚举以及随机种子的有效性，并验证异步任务创建与查询在时序上的一致性。系统对prompt进行不可打印字符清理并验证其不超过800字符；分辨率size仅允许取1280*720、720*1280等标准多媒体枚举，视频时长固定为5秒。控制器在接收请求后创建任务，返回初始PENDING或RUNNING状态的taskId，并在后台轮询完成后，确保状态有序演进至SUCCEEDED以提供下载和播放入口。测试用例涵盖空值拦截、标准长宽比通过、非法分辨率拦截以及随机种子越界拦截等，经验证容错逻辑与越界拦截行为100%符合预期。",
            "",
            "　　6.3.3  图生视频功能测试",
            "　　图生视频功能测试验证单图输入模式与首尾帧输入模式下的参数合法性及任务生命周期控制。系统设计上单图模式必须提供imageUrl，首尾帧模式须同时提供firstFrameUrl与lastFrameUrl且两者强互斥。系统限制分辨率支持480P与720P，视频时长在3至5秒之间，随机种子介于0至2147483647。接口在参数校验通过后异步调度大模型并返回taskId。测试用例包括未选择图片拦截、单图及首尾帧合法参数通过、时长越界拦截以及图片URL非法路径校验，测试结果表明系统在复杂模式切换下具备极高的容错性。",
            "",
            "　　6.3.4  图像拓展功能测试",
            "　　图像拓展功能测试主要验证空间权限控制、外延比例与像素偏移的边界约束。执行用户必须拥有该命名空间的PICTURE_EDIT权限，系统校验xScale与yScale参数取值处于1.0至3.0之间，或像素偏移范围处于0至10000之间。用户可选择开启最佳画质（best_quality）或限制图片尺寸参数。服务层解析大模型任务响应，并最终将扩图成功后的结果写回COS临时存储以供用户确认应用。测试用例包含图片ID空值校验、合法参数创建任务、拓展倍数越界拦截以及空偏移量拦截，经验证系统边界防线完备无缺。",
            "",
            "　　6.3.5  智能对话功能测试",
            "　　智能对话功能测试重点考核对话消息结构、默认模型适配以及异步轮询管线的稳定性。接口层校验messages结构体不能为空，当model为空时自动回退至系统默认大模型。系统生成任务后将状态写入Redis（标记为PROCESSING并设置10分钟有效期），后台异步调用完成后更新状态，并支持前端进行最多60次、每次5秒的轮询检索。测试用例涵盖空消息拦截、默认模型回退、超长文本拦截、非法模型白名单过滤及未登录防越权校验，经黑盒测试所有安全防御与会话一致性机制运转正常。",
            ""
        ] + lines[end_idx:]
        with open(path_txt, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print("Successfully restored the 5 distinct technical sub-sections in 稿件-v4.txt!")
    else:
        print("Failed to locate boundaries to restore")

if __name__ == "__main__":
    main()
