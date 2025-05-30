import re

ASCII_PATTERN = r'\\x[0-9a-f]{2}'


def solution(path: str):
    total_character = 0
    override_character = 0
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            total_character += len(line)
            for seq in ('\\', '"'):
                line = line.replace(seq, '\\' + seq)
            line = '"' + line + '"'
            override_character += len(line)
    return override_character - total_character


if __name__ == '__main__':
    print(solution('input_data.txt'))
