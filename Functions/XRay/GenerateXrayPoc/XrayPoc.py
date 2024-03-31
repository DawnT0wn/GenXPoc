# X-ray生成POC按钮事件
from PyQt5.QtWidgets import QMessageBox

from Utils.parse_http import parse_http_request


def generate_xray_poc(window):
    # 获取用户输入的HTTP请求
    http_request = window.ui.textEdit_6.toPlainText()

    # 解析HTTP请求
    method, path, headers, body = parse_http_request(http_request)


    poc_name = window.ui.lineEdit_7.text()
    # 构建 POC YAML
    poc_yaml = f'name: {poc_name}\n'
    poc_yaml += 'transport: http\n\n'
    if window.ui.checkBox_10.isChecked():
        poc_yaml += 'set:\n'
        poc_yaml += '  randInt0: randomInt(1000, 9999)\n'
        poc_yaml += '  randStr1: randomLowercase(10)\n'
        poc_yaml += '  reverse: newReverse()\n'
        poc_yaml += '  reverseURL: reverse.url\n\n'
    poc_yaml += '# 匹配规则\n'
    poc_yaml += 'rules:\n'
    poc_yaml += '  r1:\n'
    poc_yaml += '    request:\n'
    if window.ui.checkBox_9.isChecked():
        poc_yaml += f'      follow_redirects: true\n'
    else:
        poc_yaml += f'      follow_redirects: false\n'
    poc_yaml += f'      method: {method}\n'
    poc_yaml += f'      path: {path}\n'
    if window.ui.checkBox_11.isChecked():
        poc_yaml += '      headers:\n'
        for key, value in headers.items():
            poc_yaml += f'        {key}: \'{value}\'\n'
    poc_yaml += f'      body: |\n'
    poc_yaml += f'        {body}\n'
    poc_yaml += '      expression: |\n'
    poc_yaml += f'        {window.ui.lineEdit_9.text()}\n\n'
    if window.ui.checkBox_13.isChecked():
        poc_yaml += '      output:\n'
        poc_yaml += '        search: |\n'
        poc_yaml += '            r\'(?P<info>\\|.*\\|)\'.bsubmatch(response.raw)\n'
        poc_yaml += '        info: search["info"]\n\n'
    poc_yaml += '# rule执行顺序\n'
    poc_yaml += 'expression: r1()\n\n'
    poc_yaml += 'detail:\n'
    poc_yaml += f'  author: {window.ui.lineEdit_5.text()}\n'

    # 在文本框中显示生成的POC
    window.ui.textEdit_8.setPlainText(poc_yaml)

    # 可以选择性地显示消息框提示用户生成完成
    QMessageBox.information(window, "生成完成", "新的X-ray POC已生成")
