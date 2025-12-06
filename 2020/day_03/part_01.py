DOWN = 1
RIGHT = 3


def read_data(path: str):
    with open(path, 'r') as file:
        while line := file.readline():
            yield line.strip()


def solution(path: str):
    result, idx = 0, 0
    for row, line in enumerate(read_data(path)):
        if row:
            if line[idx] == '#':
                result += 1
        idx = (idx + RIGHT) % len(line)
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
