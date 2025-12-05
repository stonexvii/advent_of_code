def read_data(path: str):
    with open(path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]


def solution(path: str):
    deep_map = read_data(path)
    result = 0
    current = deep_map[0]
    for deep in deep_map:
        if deep > current:
            result += 1
        current = deep
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
