# 保存POC按钮相关功能
import os
import re
from PyQt5.QtWidgets import QFileDialog

# 用户查找POC中的id: xxx的字符串便于保存poc命名
def generate_filename(content):
    # 在内容中查找形如 "id: xxx" 的字符串
    match = re.search(r'name:\s*(\S+)', content)
    if match:
        # 提取出id并组合成文件名
        return match.group(1) + ".yaml"
    else:
        return "default" + ".yaml"  # 如果没有找到id，则使用默认文件名

def save_xray_poc(window):
    options = QFileDialog.Options()
    # 获取 templates 文件夹的路径（相对于当前脚本的父目录）
    current_dir = os.path.abspath(".")
    templates_folder_path = os.path.join(current_dir, 'templates')
    # 获取 textEdit_8 中的内容
    content = window.ui.textEdit_8.toPlainText()
    # 获取选中的单选框，以便定位到不同的POC文件夹，保存poc时方便打开
    selected_tool = "X-ray"
    # 生成默认文件名
    default_filename = generate_filename(content)
    # 打开文件对话框并填充默认文件夹和文件名
    file_name, _ = QFileDialog.getSaveFileName(window, "保存文件", os.path.join(templates_folder_path, selected_tool, default_filename), "YAML Files (*.yaml);;Text Files (*.txt);;All Files (*)", options=options)
    if file_name:
        # 拼接文件路径
        file_path = file_name
        # 将内容保存到文件中
        with open(file_path, 'w') as file:
            file.write(content)

