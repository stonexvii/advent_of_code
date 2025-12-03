MAX_CELLS = 12


def read_data(path: str):
    with open(path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def get_max(line: list[int]):
    idx, k = 0, MAX_CELLS - 1
    result = []
    while len(result) < MAX_CELLS:
        max_int = max(line[idx:len(line) - k])
        result.append(max_int)
        idx = line.index(max_int, idx) + 1
        k -= 1
    return result


def solution(path: str):
    result = 0
    for line in read_data(path):
        get_max(line)
        result += int(''.join(list(map(str, get_max(line)))))
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
