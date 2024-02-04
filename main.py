import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QFileDialog, \
    QComboBox, QLabel, QStackedWidget


class MyTool(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("GenXPoc")

        # 创建左边窗口
        self.left_window = QTextEdit()

        # 创建切换按钮
        self.nuclei_button = QPushButton("Nuclei")
        self.xray_button = QPushButton("X-ray")

        # 创建文件选择按钮和下拉菜单
        self.browse_button = QPushButton("浏览文件夹")
        self.file_combobox = QComboBox()

        # 创建右边窗口
        self.right_window_nuclei = QTextEdit()
        self.right_window_nuclei.setReadOnly(True)

        self.right_window_xray = QTextEdit()
        self.right_window_xray.setReadOnly(True)

        # 创建解析按钮
        self.parse_button = QPushButton("解析")
        self.parse_button.clicked.connect(self.parse_input)

        # 设置按钮点击事件
        self.nuclei_button.clicked.connect(lambda: self.switch_content("Nuclei"))
        self.xray_button.clicked.connect(lambda: self.switch_content("X-ray"))
        self.browse_button.clicked.connect(self.browse_folder)

        # 设置布局
        self.nuclei_layout = QVBoxLayout()
        self.nuclei_layout.addWidget(QLabel("Nuclei 布局"))
        self.nuclei_layout.addWidget(self.left_window)
        self.nuclei_layout.addWidget(self.parse_button)
        self.nuclei_layout.addWidget(QLabel("解析结果:"))
        self.nuclei_layout.addWidget(self.right_window_nuclei)

        self.xray_layout = QVBoxLayout()
        self.xray_layout.addWidget(QLabel("X-ray 布局"))
        self.xray_layout.addWidget(self.left_window)
        self.xray_layout.addWidget(self.parse_button)
        self.xray_layout.addWidget(QLabel("解析结果:"))
        self.xray_layout.addWidget(self.right_window_xray)

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(QWidget())
        self.stacked_widget.addWidget(QWidget())
        self.stacked_widget.widget(0).setLayout(self.nuclei_layout)
        self.stacked_widget.widget(1).setLayout(self.xray_layout)

        # 设置主窗口的布局
        main_layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.nuclei_button)
        button_layout.addWidget(self.xray_button)

        browse_layout = QHBoxLayout()
        browse_layout.addWidget(self.browse_button)
        browse_layout.addWidget(self.file_combobox)

        main_layout.addLayout(browse_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)

        # 初始内容类型
        self.current_content = "Nuclei"

    def parse_input(self):
        # 获取左边窗口的内容
        input_text = self.left_window.toPlainText()

        # 在这里进行你的解析操作
        if self.current_content == "Nuclei":
            self.right_window_nuclei.setPlainText(f"Nuclei 解析结果: {input_text}")
        elif self.current_content == "X-ray":
            self.right_window_xray.setPlainText(f"X-ray 解析结果: {input_text}")

    def switch_content(self, content_type):
        # 切换内容类型
        if content_type == "Nuclei":
            self.stacked_widget.setCurrentIndex(0)
        elif content_type == "X-ray":
            self.stacked_widget.setCurrentIndex(1)
        self.current_content = content_type

    def browse_folder(self):
        # 弹出文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")

        # 遍历文件夹中的.yaml和.yml文件，将文件名添加到下拉菜单中
        if folder_path:
            yaml_files = [file for file in os.listdir(folder_path) if file.endswith((".yaml", ".yml"))]
            self.file_combobox.clear()
            self.file_combobox.addItems(yaml_files)


if __name__ == "__main__":
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 创建主窗口
    window = MyTool()
    window.show()

    # 运行应用程序
    sys.exit(app.exec())
