def parse_number(number_str):
    if number_str.endswith('万'):
        return int(float(number_str[:-1]) * 10e4)
    elif number_str.endswith('亿'):
        return int(float(number_str[:-1]) * 10e8)
    elif number_str.isdigit():
        return int(number_str)
    else:
        raise ValueError('param number_str: {} is invalid!'.format(number_str))
