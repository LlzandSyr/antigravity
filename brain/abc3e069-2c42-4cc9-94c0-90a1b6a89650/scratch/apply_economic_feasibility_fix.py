import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_economic = "经济可行性：对象存储引入冷热分离和使用CDN加速，二级缓存减少数据库回源，并通过队列削峰、空间配额与限流机制控制日常API调用开销，经济效益良好。"
    new_economic = (
        "经济可行性：系统在接入大模型服务时采用阿里云百炼平台，该平台依据模型计费接口收费。系统实施了精细的配额管理与消费控制，"
        "其中图像生成任务依据生成张数与分辨率计费，视频生成任务按照时长与分辨率计费，文本对话任务则按照输入与输出Token计费。为避免消费失控并降低接口开销，"
        "系统在前端对高耗能的分辨率、视频时长做出了限制，同时提供静态默认选择，并在后端设计了空间配额与限流机制。在研发与系统调试中，通过选用低分辨率与短时长策略，"
        "将每日接口开销控制在极低水平，确保开支安全可控。此外，对象存储服务引入冷热分离存储策略并配合CDN进行分发加速，结合二级缓存减少数据库回源，进一步降低了云资源的运行成本，经济效益显著。"
    )
    
    if old_economic in content:
        content = content.replace(old_economic, new_economic)
        with open(path_txt, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully updated economic feasibility in 稿件-v4.txt")
    else:
        print("Target economic feasibility sentence not found, searching for partial...")
        if "经济可行性" in content:
            # Let's locate the paragraph
            lines = content.splitlines()
            for idx, l in enumerate(lines):
                if "经济可行性" in l:
                    print(f"Original: {l}")
                    lines[idx] = "　　" + new_economic
            with open(path_txt, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print("Successfully updated using line-by-line replace")

if __name__ == "__main__":
    main()
