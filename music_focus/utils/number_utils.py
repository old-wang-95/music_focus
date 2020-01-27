def parse_number(number_str):
    if number_str.endswith('万'):
        return int(float(number_str[:-1]) * 10e4)
    elif number_str.endswith('亿'):
        return int(float(number_str[:-1]) * 10e8)
    else:
        return int(number_str)
