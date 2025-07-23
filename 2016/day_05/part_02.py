from hashlib import md5


def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip()


def solution(path: str):
    code = [None] * 8
    code_data = read_data(path)
    number = 0
    while not all(code):
        code_segment = code_data + str(number)
        code_hash = md5(code_segment.encode()).hexdigest()
        if code_hash.startswith('00000'):
            index = code_hash[5]
            if index.isdigit() and 0 <= int(index) < 8 and not code[int(index)]:
                code[int(index)] = code_hash[6]
        number += 1
    return ''.join(code)


if __name__ == '__main__':
    print(solution('input_data.txt'))
