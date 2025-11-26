def read_data(path: str):
    with open(path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def solution(path: str):
    data_map = read_data(path)
    row_count = len(data_map)
    line_count = len(data_map[0])
    count_visible = 2 * line_count + (row_count - 2) * 2

    def check_visible(data_line: list[int], idx: int):
        left = data_line[:idx]
        right = data_line[idx + 1:]
        current_item = data_line[idx]
        if (max(left) < current_item) or (max(right) < current_item):
            return True

    for row in range(1, row_count - 1):
        for i in range(1, line_count - 1):
            column = [data_map[k][i] for k in range(row_count)]
            if check_visible(data_map[row], i) or check_visible(column, row):
                count_visible += 1
    return count_visible


if __name__ == '__main__':
    print(solution('input_data.txt'))
