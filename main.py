import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from Functions import *
from Gui.Gen_ui import Ui_Form


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 在此处可以添加与界面相关的逻辑
        self.ui.pushButton.clicked.connect(lambda: select_poc(self))  # lambda 函数通常用于在连接信号和槽时传递额外的参数
        self.ui.pushButton_2.clicked.connect(lambda: generate_new_poc(self))
        self.ui.pushButton_3.clicked.connect(lambda: save_poc(self))
        self.ui.pushButton_4.clicked.connect(lambda: select_executable_path(self))
        self.ui.pushButton_7.clicked.connect(lambda: add_to_poc(self))
        # self.ui.pushButton_5.clicked.connect(self.save_result)
        # self.ui.pushButton_6.clicked.connect(lambda: execute(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
