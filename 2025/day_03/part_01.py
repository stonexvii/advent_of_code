def read_data(path: str):
    with open(path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def get_max(line: list[int]):
    result = []
    for i in range(len(line) - 1):
        result.append(line[i]*10 + max(line[i + 1:]))
    return result


def solution(path: str):
    result = 0
    for line in read_data(path):
        result += max(get_max(line))
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
