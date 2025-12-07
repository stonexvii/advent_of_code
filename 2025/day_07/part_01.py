def read_data(path: str):
    with open(path, 'r') as file:
        while line := file.readline():
            yield line.strip()


def solution(path: str):
    result, data_map = 0, read_data(path)
    start_idx = next(data_map).index('S')
    indexes = {0: {start_idx}}
    for row_idx, line in enumerate(data_map, 1):
        indexes[row_idx] = indexes[row_idx - 1].copy()
        for idx in indexes[row_idx - 1]:
            if line[idx] == '^':
                indexes[row_idx].remove(idx)
                indexes[row_idx].update({idx - 1, idx + 1})
                result += 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
