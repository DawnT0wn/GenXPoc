import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton

class MyTool(QWidget):
    def __init__(self):
        super().__init__()

        # 创建左边窗口
        self.left_window = QTextEdit()

        # 创建切换按钮
        self.nuclei_button = QPushButton("Nuclei")
        self.xray_button = QPushButton("X-ray")

        # 创建右边窗口
        self.right_window = QTextEdit()
        self.right_window.setReadOnly(True)

        # 创建解析按钮
        self.parse_button = QPushButton("解析")
        self.parse_button.clicked.connect(self.parse_input)

        # 设置按钮点击事件
        self.nuclei_button.clicked.connect(lambda: self.switch_content("Nuclei"))
        self.xray_button.clicked.connect(lambda: self.switch_content("X-ray"))

        # 设置布局
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.nuclei_button)
        button_layout.addWidget(self.xray_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.left_window)
        main_layout.addWidget(self.parse_button)
        main_layout.addWidget(self.right_window)

        # 设置主窗口的布局
        self.setLayout(main_layout)

        # 初始内容类型
        self.current_content = "Nuclei"

    def parse_input(self):
        # 获取左边窗口的内容
        input_text = self.left_window.toPlainText()

        # 在这里进行你的解析操作，这里简单地将输入内容设置到右边窗口
        self.right_window.setPlainText(f"{self.current_content} 解析结果: {input_text}")

    def switch_content(self, content_type):
        # 切换内容类型
        self.current_content = content_type

if __name__ == "__main__":
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 创建主窗口
    window = MyTool()
    window.show()

    # 运行应用程序
    sys.exit(app.exec())
