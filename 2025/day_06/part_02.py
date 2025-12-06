from itertools import zip_longest


def read_data(path: str):
    with open(path, 'r') as file:
        return list(zip_longest(*[list(line.strip().replace(' ', '0')) for line in file.readlines()], fillvalue='0'))


def calculate(data_line: list[str]):
    operator = data_line.pop(0)
    result = 1 if operator == '*' else 0
    for number in data_line:
        if operator == '*':
            result *= number
        else:
            result += number
    return result


def solution(path: str):
    result, temp_data, operator = 0, [], None
    for line in read_data(path):
        if line[-1] != '0':
            temp_data.append(line[-1])
        if len(set(line)) != 1:
            temp_data.append(int(''.join(line[:-1]).replace('0', '')))
        else:
            result += calculate(temp_data)
            temp_data = []
    result += calculate(temp_data)
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
