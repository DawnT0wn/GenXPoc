# Add to Poc按钮相关功能
import re


def nuclei_add_to_poc(window):
    generated_poc = window.ui.textEdit_2.toPlainText()

    # 为了在 matchers-condition 前插入新的请求，匹配其索引，调整与yaml的缩进格式
    index = generated_poc.find("matchers-condition: and")

    http_request = window.ui.textEdit.toPlainText().replace('\n', '\n        ')
    http_request = re.sub(r'Host:\s*(\S+)', r'Host: {{Hostname}}', http_request, flags=re.IGNORECASE)

    modified_poc = generated_poc[:index] + "  - |\n        " + http_request + "\n\n    " + generated_poc[index:]

    window.ui.textEdit_2.setPlainText(modified_poc)