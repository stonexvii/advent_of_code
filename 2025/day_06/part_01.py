def read_data(path: str):
    with open(path, 'r') as file:
        return list(zip(*[line.strip().split() for line in file.readlines()]))


def calculate(data_line: list[str]):
    operator = data_line.pop()
    result = 1 if operator == '*' else 0
    for number in data_line:
        if operator == '*':
            result *= int(number)
        else:
            result += int(number)
    return result


def solution(path: str):
    result = 0
    for line in read_data(path):
        result += calculate(list(line))
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
