import os
import re

# 定义源目录和目标目录（目标目录为 Rules/Shadowrocket/<NAME>）
SOURCE_DIR = "main/Rules/Clash.Meta"
TARGET_BASE = "main/Rules/Shadowrocket"

def transform_content(content):
    lines = content.splitlines()
    new_lines = []
    in_payload = False
    for line in lines:
        # 修改头部的 updata_url 行
        if line.startswith("# updata_url:"):
            # 将 <url ... 的 URL 地址替换为指定目标地址
            new_line = re.sub(
                r"https://raw\.githubusercontent\.com/LaolunsiG/PCR/main/Rules/Clash\.Meta/",
                "https://github.com/LaolunsiG/PCR/raw/heads/main/Rules/Shadowrocket/",
                line
            )
            # 替换文件扩展名
            new_line = re.sub(r"\.yaml(\s*)$", ".list", new_line)
            new_lines.append(new_line)
            continue
        
        # 修改 repo 行，将 Clash.Meta 替换为 Shadowrocket
        if line.startswith("# repo:"):
            new_line = re.sub(r"Clash\.Meta", "Shadowrocket", line)
            new_lines.append(new_line)
            continue
        
        # 检查 payload 行，遇到 payload: 则开始处理 payload 块
        if line.strip() == "payload:":
            in_payload = True
            continue  # 跳过 payload: 这一行
        
        if in_payload:
            # 去掉前导空白
            stripped = line.lstrip()
            # 如果以 "- " 开头，进行处理
            if stripped.startswith("- "):
                # 如果是 - IP-CIDR, 开头，则转换为注释形式
                if stripped.startswith("- IP-CIDR,"):
                    new_line = f"#{stripped[2:]}"
                else:
                    new_line = stripped[2:]
                new_lines.append(new_line)
            else:
                # 对于已经是注释的行，去掉前面的空格
                new_lines.append(stripped)
        else:
            new_lines.append(line)
    
    # 添加一个空行，避免最后一行没有换行符
    return "\n".join(new_lines) + "\n"


def get_name_from_content(content):
    # 从 "# NAME: Airport" 这类行中提取名称
    match = re.search(r"^# NAME:\s*(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip().title()  # 首字母大写
    return "Unknown"


def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"源目录 '{SOURCE_DIR}' 不存在。")
        return

    # 遍历源目录中的所有文件
    for filename in os.listdir(SOURCE_DIR):
        source_path = os.path.join(SOURCE_DIR, filename)
        # 确保是文件
        if os.path.isfile(source_path):
            try:
                with open(source_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"读取文件 '{source_path}' 时出错: {e}")
                continue

            # 获取文件内容，并进行转换
            transformed_content = transform_content(content)

            # 获取文件名称
            name = get_name_from_content(content)
            # 跳过未知名称的文件
            if name == "Unknown":
                print(f"跳过文件 '{filename}'，未找到 NAME。")
                continue

            # 目标目录路径
            target_dir = os.path.join(TARGET_BASE, name)
            os.makedirs(target_dir, exist_ok=True)  # 创建目标目录

            # 文件扩展名处理
            base, ext = os.path.splitext(filename)
            if ext.lower() == ".yaml":
                target_filename = f"{base}.list"
            else:
                target_filename = filename

            target_path = os.path.join(target_dir, target_filename)

            try:
                with open(target_path, "w", encoding="utf-8") as f:
                    f.write(transformed_content)
                print(f"已处理 {source_path} -> {target_path}")
            except Exception as e:
                print(f"写入文件 '{target_path}' 时出错: {e}")


if __name__ == "__main__":
    main()
