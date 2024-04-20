from Utils import *
import os
import subprocess
from applescript import tell
from PyQt5.QtWidgets import QMessageBox
import platform
from Config import *

def execute_xray(window):
    selected_poc = window.ui.comboBox_4.currentText()
    if selected_poc == "":
        QMessageBox.information(window, "Execute POC", "Please Select Your POC!!!")
        return None

    url = validate_and_get_url(window.ui.textEdit_7.toPlainText())
    if url is None:
        QMessageBox.information(window, "Invaild URL", "Please input only one valid URL")
        return None

    poc_path = get_xrry_poc_path() + "/" + selected_poc

    execute_path = window.ui.lineEdit_8.text()

    if window.ui.checkBox_14.isChecked():
        current_dir = os.path.abspath(".")
        result_folder_path = os.path.join(current_dir, "Results")
        filename = result_folder_path + "/" + selected_poc.split(".")[0]
        output_file_type = window.ui.comboBox_5.currentText()
        if output_file_type == "html":
            command = [execute_path, "--log-level", "debug", "webscan", "--url", url, "-p", poc_path, "--html-output", f"{filename}.html"]
        if output_file_type == "json":
            command = [execute_path, "--log-level", "debug", "webscan", "--url", url, "-p", poc_path, "--json-output", f"{filename}.json"]
    else:
        command = [execute_path, "--log-level", "debug", "webscan", "--url", url, "-p", poc_path]

    job_path = os.path.dirname(execute_path)

    os_name = platform.system()
    command = " ".join(command)
    if os_name == 'Darwin':
        tell.app('Terminal', 'do script"' + f"cd {job_path} &&" + command + '"')
    elif os_name == 'Windows':
        cmd_command = f'start cmd.exe @cmd /k {command}'
        # Popen 不会等待命令执行完成
        process = subprocess.Popen(cmd_command, shell=True, cwd=job_path)