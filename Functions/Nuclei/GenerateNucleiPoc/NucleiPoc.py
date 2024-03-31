# Nuclei POC生成相关逻辑

import re
from PyQt5.QtWidgets import QMessageBox

from Functions.Nuclei.GenerateNucleiPoc.Extractors import GetExtractors
from Functions.Nuclei.GenerateNucleiPoc.Machers import GetMatchers


def generate_nuclei_poc(window):
    # 获取 HTTP 请求内容
    http_request = window.ui.textEdit.toPlainText().replace('\n', '\n        ')

    # 使用正则表达式替换 Host 部分为 {{Hostname}}
    http_request = re.sub(r'Host:\s*(\S+)', r'Host: {{Hostname}}', http_request, flags=re.IGNORECASE)

    # 从界面上获取模版信息
    template_id = window.ui.lineEdit_4.text()
    template_name = window.ui.lineEdit_2.text()
    template_author = window.ui.lineEdit_3.text()
    template_severity = window.ui.comboBox_3.currentText()
    matchers = GetMatchers(window)
    extractors = GetExtractors(window)

    if len(matchers) != 0:
    # 构建 Nuclei POC
        nuclei_poc = f'''id: {template_id}

info:
  name: {template_name}
  author: {template_author}
  severity: {template_severity}

requests:
  - raw:
      - |
        {http_request}

    matchers-condition: and
    matchers:
{chr(10).join(matchers)}
{chr(10).join(extractors)}
'''
    else:
        nuclei_poc = f'''id: {template_id}

info:
  name: {template_name}
  author: {template_author}
  severity: {template_severity}

requests:
  - raw:
      - |
        {http_request}

    matchers-condition: and
{chr(10).join(extractors)}
'''

    # 将生成的 Nuclei POC 写入 textEdit_2
    window.ui.textEdit_2.setPlainText(nuclei_poc)

    # 提示用户 Nuclei POC 已生成
    QMessageBox.information(window, "Nuclei POC Generated",
                            "Nuclei POC has been generated and updated in the text area.")
