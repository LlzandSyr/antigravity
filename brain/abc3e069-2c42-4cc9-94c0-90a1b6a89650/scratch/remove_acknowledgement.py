import os

def main():
    path_txt = r"C:\Users\86135\Desktop\优秀毕业论文\稿件-v4.txt"
    if not os.path.exists(path_txt):
        print("File not found")
        return
        
    with open(path_txt, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We find "致        谢" or "致\t谢" or "致    谢"
    # To be extremely robust, we can use regex or find borders
    idx_ack = content.find("致        谢")
    if idx_ack == -1:
        # Check standard Chinese characters
        idx_ack = content.find("致谢")
    if idx_ack == -1:
        # Check with other white spaces
        for i in range(1, 20):
            spaces = " " * i
            idx_ack = content.find(f"致{spaces}谢")
            if idx_ack != -1:
                break
                
    if idx_ack == -1:
        print("Could not find Acknowledgement start")
        return
        
    idx_eng_title = content.find("Design and Implementation of a Multimodal AI Gallery System")
    if idx_eng_title == -1:
        print("Could not find English title")
        return
        
    # Delete everything between idx_ack and idx_eng_title
    # But leave a clean double newline separator
    content_new = content[:idx_ack].rstrip() + "\n\n\n" + content[idx_eng_title:]
    
    with open(path_txt, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(content_new)
        
    print("Acknowledgement section deleted successfully!")

if __name__ == "__main__":
    main()
