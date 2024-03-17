# 生成新的POC相关逻辑
from Functions.GenerateNewPoc.NucleiPoc import generate_nuclei_poc


def generate_new_poc(window):
    # 感觉单选框选中的扫描器类型进入到不同的生成逻辑，也方便二次开发扩展
    if window.ui.radioButton.isChecked():
        selected_tool = "Nuclei"    # 无实际作用，标明选择的扫描器类型
        generate_nuclei_poc(window)
    elif window.ui.radioButton_2.isChecked():
        selected_tool = "X-ray"