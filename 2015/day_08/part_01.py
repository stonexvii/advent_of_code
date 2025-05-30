import re

ASCII_PATTERN = r'\\x[0-9a-f]{2}'


def solution(path: str):
    total_character = 0
    necessary_character = 0
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            total_character += len(line)
            line = line[1:-1].replace('\\\\', '!')
            if line.count('\\x'):
                result = re.findall(ASCII_PATTERN, line)
                for sequence in result:
                    line = line.replace(sequence, 'A')
            line = line.replace('\\', '')
            necessary_character += len(line)
    return total_character - necessary_character


if __name__ == '__main__':
    print(solution('input_data.txt'))
