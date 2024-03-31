# and last poc按钮事件
import yaml

from Utils.parse_http import parse_http_request

def and_last_xray_poc(window):
    # 获取用户输入的HTTP请求
    http_request = window.ui.textEdit_6.toPlainText()

    # 解析HTTP请求
    method, path, headers, body = parse_http_request(http_request)

    generated_poc = window.ui.textEdit_8.toPlainText()
    poc_dict = yaml.safe_load(generated_poc)
    rule_count = len(poc_dict['rules'])
    expression = poc_dict["expression"]

    # 构建新的规则
    new_rule_yaml = '  r{}:\n'.format(rule_count + 1)
    new_rule_yaml += '    request:\n'
    new_rule_yaml += f'      method: {method}\n'
    new_rule_yaml += f'      path: {path}\n'
    new_rule_yaml += f'      body: |\n'
    new_rule_yaml += f'        {body}\n'
    if window.ui.checkBox_9.isChecked():
        new_rule_yaml += f'      follow_redirects: true\n'
    else:
        new_rule_yaml += f'      follow_redirects: false\n'
    if window.ui.checkBox_11.isChecked():
        new_rule_yaml += '      headers:\n'
        for key, value in headers.items():
            new_rule_yaml += f'        {key}: \'{value}\'\n'
    new_rule_yaml += '    expression: |\n'
    new_rule_yaml += f'      {window.ui.lineEdit_9.text()}\n'
    if window.ui.checkBox_13.isChecked():
        new_rule_yaml += '    output:\n'
        new_rule_yaml += '      search: |\n'
        new_rule_yaml += '        r\'(?P<info>\\|.*\\|)\' bsubmatch(response.raw)\n'
        new_rule_yaml += '      info: search["info"]\n\n'

    poc_yaml_list = generated_poc.split('\n')
    expression_index = poc_yaml_list.index(f'expression: {expression}')
    poc_yaml_list.insert(expression_index, new_rule_yaml)

    # 更新 poc_yaml 字符串
    poc_yaml_updated = '\n'.join(poc_yaml_list)
    new_expression = f'{expression} && r{rule_count + 1}()'
    poc_yaml_updated = poc_yaml_updated.replace(f"expression: {expression}", f"expression: {new_expression}")

    window.ui.textEdit_8.setPlainText(poc_yaml_updated)
