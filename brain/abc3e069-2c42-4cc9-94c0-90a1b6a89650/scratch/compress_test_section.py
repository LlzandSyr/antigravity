import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("Text file not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We will locate 6.3 and replace everything from 6.3 up to 6.4 with the single paragraph!
    lines = content.splitlines()
    start_idx = -1
    end_idx = -1
    for idx, l in enumerate(lines):
        if "6.3  测试用例" in l or "6.3 测试用例" in l:
            start_idx = idx
        if start_idx != -1 and "6.4  测试结论" in l or "6.4 测试结论" in l:
            end_idx = idx
            break
            
    if start_idx != -1 and end_idx != -1:
        new_lines = lines[:start_idx] + [
            "6.3  测试用例与核心逻辑",
            "　　本研究针对系统核心的文生图、文生视频、图生视频、图像拓展与智能对话五大多模态AIGC功能开展黑盒边界测试。测试涵盖了参数校验与防越权安全防御两类核心场景：在权限校验上，系统基于Sa-Token对命名空间下的PICTURE_EDIT等敏感权限进行严格拦截与未登录鉴权；在参数边界校验上，文生图与文生视频接口重点验证了800字符以内的prompt合法性限制、1至4张的生成数量、0至2147483647范围的随机种子、标准多媒体分辨率枚举及固定时长的约束；图生视频接口则严格验证了单图模式与首尾帧模式的互斥关系，限制视频时长在3至5秒；图像拓展接口对xScale与yScale参数处于1.0至3.0之间及像素偏移处于0至10000之间的外延边界进行了充分校验；智能对话接口则重点验证了messages不能为空、模型留空自动回退及Redis中PROCESSING异步状态流转等管线逻辑。黑盒测试结果表明，系统在复杂边界、空值拦截、非法参数及越权操作等组合场景下均能实现精准防御，整体容错与安全机制运转正常。",
            ""
        ] + lines[end_idx:]
        with open(path_txt, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        print("Successfully compressed test case section to a single paragraph in 稿件-v4.txt!")
    else:
        print("Failed to locate boundaries for compression")

if __name__ == "__main__":
    main()
