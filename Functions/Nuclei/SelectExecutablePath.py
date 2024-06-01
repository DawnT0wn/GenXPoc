from PyQt5.QtWidgets import QFileDialog
from Config import *

# 设计选择可执行文件路径
def select_executable_nuclei_path(window):
    binary_nuclei_path = get_binary_nuclei()
    window.ui.lineEdit.setText(binary_nuclei_path)

    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(window, "选择可执行文件路径", "",
                                               "All Files (*);;Executable Files (*.exe)", options=options)
    # All Files ();;Executable Files (.exe) 是一个文件过滤器，用于限制用户在文件对话框中选择的文件类型。
    #
    # All Files (*) 表示用户可以选择任何类型的文件，因为 * 通配符匹配所有文件类型。这意味着用户可以选择任何文件。
    # Executable Files (*.exe) 表示用户只能选择可执行文件，并且文件名必须以 .exe 结尾。
    # 因此，当用户在文件对话框中打开文件时，他们将只能选择 .exe 格式的文件，或者是任何其他类型的文件。
    if file_path:
        window.ui.lineEdit.setText(file_path)  # 将选定的路径显示在文本框中
        set_binary_nuclei(file_path)