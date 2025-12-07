from functools import lru_cache


def read_data(path: str):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def solution(path: str):
    data_map = read_data(path)
    start_idx = data_map[0].index('S')

    @lru_cache()
    def split_ray(row_line: int, idx: int):
        for row_idx, line in enumerate(data_map[row_line:], row_line):
            if line[idx] == '^':
                return split_ray(row_idx, idx - 1) + split_ray(row_idx, idx + 1)
            if row_idx == len(data_map) - 1:
                return 1

    result = split_ray(0, start_idx)
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
