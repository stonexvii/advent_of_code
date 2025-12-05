def read_data(path: str):
    with open(path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]


def solution(path: str):
    deep_map = read_data(path)
    result = 0
    current = sum(deep_map[:3])
    for idx in range(1, len(deep_map)):
        sum_slice = sum(deep_map[idx:idx+3])
        if sum_slice > current:
            result += 1
        current = sum_slice
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
