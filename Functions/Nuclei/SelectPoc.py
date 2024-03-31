import os
from PyQt5.QtWidgets import QFileDialog
from Config import *

# 添加选择POC的逻辑
def select_nuclei_poc(window):
    options = QFileDialog.Options()
    folder_path = QFileDialog.getExistingDirectory(window, "选择文件夹", options=options)
    if folder_path:
        window.ui.comboBox_2.clear()  # 清除之前的内容
        for file_name in os.listdir(folder_path):
            if file_name.endswith(('.yaml', '.yml')):
                window.ui.comboBox_2.addItem(file_name)
                set_nuclei_poc_path(folder_path)