def GetExtractors(window):
    # Extractors部分
    extractors = []
    if window.ui.checkBox_8.isChecked():  # 如果 extractors 复选框被选中
        extractor = '''\
    extractors:
       - part: header
         internal: true
         group: 1
         type: regex
         regex:
           - 'Set-Cookie: PHPSESSID=(.*); path=/'
'''
        extractors.append(extractor)

    return extractors