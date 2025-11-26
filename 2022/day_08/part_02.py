def read_data(path: str):
    with open(path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def solution(path: str):
    data_map = read_data(path)
    row_count = len(data_map)
    line_count = len(data_map[0])
    visible_list = []

    def check_visible(data_line: list[int], idx: int):
        left_visible, right_visible = 0, 0
        left = data_line[:idx]
        right = data_line[idx + 1:]
        current_item = data_line[idx]
        for tree in left[::-1]:
            left_visible += 1
            if tree >= current_item:
                break
        for tree in right:
            right_visible += 1
            if tree >= current_item:
                break
        return left_visible, right_visible

    for row in range(1, row_count - 1):
        for i in range(1, line_count - 1):
            column = [data_map[k][i] for k in range(row_count)]
            left, right = check_visible(data_map[row], i)
            up, down = check_visible(column, row)
            visible_list.append(left * right * up * down)
    return max(visible_list)


if __name__ == '__main__':
    print(solution('input_data.txt'))
