# # 运行扫描器

import os
import subprocess
from applescript import tell
from PyQt5.QtWidgets import QMessageBox
import platform
from Utils import *
from Config import *

def execute_nuclei(window):
    selected_poc = window.ui.comboBox_2.currentText()
    if selected_poc == "":
        QMessageBox.information(window, "Execute POC", "Please Select Your POC!!!")
        return None

    url = validate_and_get_url(window.ui.textEdit_3.toPlainText())
    if url is None:
        QMessageBox.information(window, "Invaild URL", "Please input only one valid URL")
        return None

    poc_path = get_nuclei_poc_path() + "/" + selected_poc

    execute_path = window.ui.lineEdit.text()

    if window.ui.checkBox_12.isChecked():
        output_file_type = window.ui.comboBox.currentText()
        current_dir = os.path.abspath(".")
        result_folder_path = os.path.join(current_dir, "Results")
        filename = result_folder_path + "/" + selected_poc.split(".")[0]
        if output_file_type == "text":
            command = [execute_path, "-t", poc_path, "-u", url, "-o", filename]
        if output_file_type == "markdown":
            command = [execute_path, "-t", poc_path, "-u", url, "-me", f"{filename}.md"]
        if output_file_type == "json":
            command = [execute_path, "-t", poc_path, "-u", url, "-json-export", f"{filename}.json"]
    else:
        command = [execute_path, "-t", poc_path, "-u", url]

    os_name = platform.system()
    command = " ".join(command)
    if os_name == 'Darwin':
        tell.app('Terminal', 'do script"' + command + '"')
    elif os_name == 'Windows':
        cmd_command = f'start cmd.exe @cmd /k {command}'
        # Popen 不会等待命令执行完成
        process = subprocess.Popen(cmd_command, shell=True)