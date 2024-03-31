import validators

def is_valid_url(url):
    # 验证 URL 是否有效
    if validators.url(url):
        return True
    else:
        return False

def validate_and_get_url(text_content):

    # 使用 splitlines 方法将文本内容按行拆分成列表
    lines = text_content.splitlines()

    # 如果列表长度不为1，说明输入的不止一个 URL
    if len(lines) != 1:
        return None

    # 获取第一个 URL
    url = lines[0]

    # 验证 URL 是否有效
    if is_valid_url(url):
        return url
    else:
        return None