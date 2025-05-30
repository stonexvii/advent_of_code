def data_reader(path: str) -> list[tuple[str, int]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip().split()[:-1], file.readlines()))
    data = list(map(lambda x: (x[0], int(x[1])), data))
    return data


class Cell:
    def __init__(self, value: str, row: int, index: int):
        self.value = value
        self.row = row
        self.index = index
        self.visited = False



def fill_void(data_field: list[list[Cell]], start_row: int, start_index: int):
    fill_queue = [data_field[start_row][start_index]]
    while fill_queue:
        cur_cell = fill_queue.pop(0)
        cur_cell.value = '#'
        for move in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            row = cur_cell.row + move[0]
            index = cur_cell.index + move[1]
            if 0 <= row < len(data_field) and 0 <= index < len(data_field[row]) and data_field[row][index].value == '.':
                fill_queue.append(data_field[row][index])


def print_field(field_data: list[list[Cell]]):
    for row in field_data:
        for cell in row:
            print(f'{cell.value:^3}', end='')
        print()

def switch_value(mark: str):
    if mark == '#':
        return '.'
    return '#'


def solution(move_data: list[tuple[str, int]]) -> int:
    direction = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    row, index = 0, 0
    cells_index = []
    for move in move_data:
        for _ in range(move[1]):
            cells_index.append((row, index))
            next_row, next_index = direction[move[0]]
            row += next_row
            index += next_index
    min_row, max_row = min(cells_index, key=lambda x: x[0])[0], max(cells_index, key=lambda x: x[0])[0]
    min_str, max_str = min(cells_index, key=lambda x: x[1])[1], max(cells_index, key=lambda x: x[1])[1]
    cells_index = sorted(list(map(lambda x: (x[0] - min_row, x[1] - min_str), cells_index)))

    height = max_row - min_row
    width = max_str - min_str
    # i = 0
    # new_indexes = []
    # new_row = []
    # while i < len(cells_index) - 1:
    #     if cells_index[i][1] + 1 == cells_index[i+1][1]:
    #         new_row.append(cells_index[i])
    #     else:
    #         new_row = []
    #     i += 1
    #     new_indexes += new_row[1:]

    # cells_index = set(cells_index).difference(set(new_indexes))
    map_table = []
    # value = '.'
    print(cells_index)
    for row in range(height):
        new_row = []
        for index in range(width):
            if (row,index) in set(cells_index):
                # value = switch_value(value)
                value = '#'
            else:
                value = '.'
            new_row.append(Cell(value, row, index))
        map_table.append(new_row)

    start_point = 0
    for row in range(height):
        start_points = []
        if not start_point:
            for cell in cells_index:
                if cell[0] == row:
                    start_points.append(cell)
            start_points = sorted(start_points, key=lambda x: x[1])
            for i in range(len(start_points)-1):
                if start_points[i+1][1] - start_points[i][1] > 1:
                    start_point = (row, start_points[i][1] + 1)
                    break
    fill_void(map_table, start_point[0], start_point[1])
    print_field(map_table)





data = data_reader('input_data.txt')
solution(data)
