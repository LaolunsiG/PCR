import os
import re

# 定义源目录和目标目录（目标目录为 Rules/Shadowrocket/<NAME>）
source_dir = "loon"
target_base = os.path.join("Rules", "Shadowrocket")

def transform_content(content):
    lines = content.splitlines()
    new_lines = []
    in_payload = False
    for line in lines:
        # 修改头部的 updata_url 行
        if line.startswith("# updata_url:"):
            # 将 https://raw.githubusercontent.com/LaolunsiG/PCR/main/Rules/Clash.Meta/ 替换为新地址前缀
            new_line = re.sub(
                r"https://raw\.githubusercontent\.com/LaolunsiG/PCR/main/Rules/Clash\.Meta/",
                "https://github.com/LaolunsiG/PCR/raw/refs/heads/main/Rules/Shadowrocket/",
                line
            )
            # 将文件扩展名从 .yaml 改为 .list
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
                    new_line = "#" + stripped[2:]
                else:
                    new_line = stripped[2:]
                new_lines.append(new_line)
            else:
                # 对于已经是注释的行，去掉前面的空格
                new_lines.append(stripped)
        else:
            new_lines.append(line)
    return "\n".join(new_lines) + "\n"

def get_name_from_content(content):
    # 从 "# NAME: Airport" 这类行中提取名称，用于确定目标子目录
    match = re.search(r"^# NAME:\s*(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Unknown"

def main():
    if not os.path.isdir(source_dir):
        print(f"源目录 '{source_dir}' 不存在。")
        return

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_path):
            with open(source_path, "r", encoding="utf-8") as f:
                content = f.read()
            transformed = transform_content(content)
            # 根据 "# NAME:" 行确定目标目录
            name = get_name_from_content(content)
            target_dir = os.path.join(target_base, name)
            os.makedirs(target_dir, exist_ok=True)
            # 如果文件扩展名为 .yaml，则更改为 .list；否则保持原文件名
            base, ext = os.path.splitext(filename)
            if ext.lower() == ".yaml":
                target_filename = base + ".list"
            else:
                target_filename = filename
            target_path = os.path.join(target_dir, target_filename)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(transformed)
            print(f"已处理 {source_path} -> {target_path}")

if __name__ == "__main__":
    main()
