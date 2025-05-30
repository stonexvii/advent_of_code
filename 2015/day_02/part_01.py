from itertools import combinations


def read_data(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        data = [list(map(int, line.strip().split('x'))) for line in file.readlines()]
    return data


def solution(path: str):
    data = read_data(path)
    result = 0
    for entry in data:
        entry = list(combinations(entry, 2))
        for combo in entry:
            result += (combo[0] * combo[1]) * 2
        minimal = min(entry, key=lambda x: x[0] * x[1])
        result += minimal[0] * minimal[1]
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
