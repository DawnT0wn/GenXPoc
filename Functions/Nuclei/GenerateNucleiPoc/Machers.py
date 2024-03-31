# 设置Matchers

def GetMatchers(window):
    # 构建匹配器部分
    matchers = []

    if window.ui.checkBox.isChecked():  # 如果 word 复选框被选中
        word_matcher = '''\
        - type: word
          part: body
          words:
            - 'test1'
            - 'test2'
          condition: or
    '''
        matchers.append(word_matcher)

    if window.ui.checkBox_2.isChecked():  # 如果 dns 复选框被选中
        dns_matcher = '''\
        - type: word
          part: interactsh_protocol  # 配合 {{interactsh-url}} 关键词使用
          words:
            - "http"
            - "dns"
    '''
        matchers.append(dns_matcher)

    if window.ui.checkBox_3.isChecked():  # 如果 header 复选框被选中
        header_matcher = '''\
            - type: word
              part: header
              words:
                - 'apache'
        '''
        matchers.append(header_matcher)

    if window.ui.checkBox_4.isChecked():    # 如果 dsl 复选框被选中
        dsl_matcher = '''
            - type: dsl
              dsl:
              - 'len(body)<130'
              - 'duration>=6'
        '''
        matchers.append(dsl_matcher)

    if window.ui.checkBox_5.isChecked():  # 如果 status 复选框被选中
        status_matcher = '''\
            - type: status
              status:
                - 200
        '''
        matchers.append(status_matcher)

    if window.ui.checkBox_6.isChecked():  # 如果 Binary 复选框被选中
        binary_matcher = '''\
            - type: binary
              binary:
              - "D0CF11E0"  # db
              - "53514C69746520"  # SQLite
            part: body
            condition: or
        '''
        matchers.append(binary_matcher)

    if window.ui.checkBox_7.isChecked():  # 如果 Regex 复选框被选中
        regex_matcher = '''\
            - type: regex
              regex:
                - "root:.*:0:0:"
              part: body
        '''
        matchers.append(regex_matcher)


    return matchers