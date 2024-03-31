def parse_http_request(http_request):
    method = ''
    path = ''
    headers = {}
    body = ''

    lines = http_request.strip().split('\n')
    # 解析请求行
    request_line_parts = lines[0].strip().split(' ')
    method = request_line_parts[0]
    path = request_line_parts[1]

    # 解析请求头和请求体
    is_body = False
    for line in lines[1:]:
        if line.strip() == '':
            is_body = True
            continue
        if ':' in line:
            key, value = line.strip().split(':', 1)
            if key.lower() != 'host':  # 忽略Host字段
                headers[key.strip()] = value.strip()
        elif is_body:
            body += line.strip()

    return method, path, headers, body