import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from Functions import *
from Gui.Gen_ui import Ui_Form


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化可执行文件路径
        self.ui.lineEdit.setText(get_binary_nuclei())
        self.ui.lineEdit_8.setText(get_binary_xray())

        # 在此处设计Nuclei界面可以添加与界面相关的逻辑
        self.ui.pushButton.clicked.connect(lambda: select_nuclei_poc(self))  # lambda 函数通常用于在连接信号和槽时传递额外的参数
        self.ui.pushButton_2.clicked.connect(lambda: generate_nuclei_poc(self))
        self.ui.pushButton_3.clicked.connect(lambda: save_nuclei_poc(self))
        self.ui.pushButton_4.clicked.connect(lambda: select_executable_nuclei_path(self))
        self.ui.pushButton_7.clicked.connect(lambda: nuclei_add_to_poc(self))
        self.ui.pushButton_6.clicked.connect(lambda: execute_nuclei(self))

        # 此处为Xray界面相关事件绑定
        self.ui.pushButton_14.clicked.connect(lambda: select_executable_xray_path(self))
        self.ui.pushButton_11.clicked.connect(lambda: select_xray_poc(self))
        self.ui.pushButton_10.clicked.connect(lambda: save_xray_poc(self))
        self.ui.pushButton_12.clicked.connect(lambda: generate_xray_poc(self))
        self.ui.pushButton_13.clicked.connect(lambda: and_last_xray_poc(self))
        self.ui.pushButton_5.clicked.connect(lambda: or_last_xray_poc(self))
        self.ui.pushButton_9.clicked.connect(lambda: execute_xray(self))

if __name__ == "__main__":
    load_config()
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
