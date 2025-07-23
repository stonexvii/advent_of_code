from hashlib import md5


def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip()


def solution(path: str):
    code = ''
    code_data = read_data(path)
    number = 0
    while len(code) < 8:
        code_segment = code_data + str(number)
        code_hash = md5(code_segment.encode()).hexdigest()
        if code_hash.startswith('00000'):
            code += code_hash[5]
        number += 1
    return code


if __name__ == '__main__':
    print(solution('input_data.txt'))
