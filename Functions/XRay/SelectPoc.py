# Xray界面选择POC按钮

import os
from PyQt5.QtWidgets import QFileDialog

from Config import set_xray_poc_path


# 添加选择POC的逻辑
def select_xray_poc(window):
    options = QFileDialog.Options()
    folder_path = QFileDialog.getExistingDirectory(window, "选择文件夹", options=options)
    if folder_path:
        window.ui.comboBox_4.clear()  # 清除之前的内容
        for file_name in os.listdir(folder_path):
            if file_name.endswith(('.yaml', '.yml')):
                window.ui.comboBox_4.addItem(file_name)
                set_xray_poc_path(folder_path)