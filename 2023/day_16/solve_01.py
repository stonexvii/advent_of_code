class Cell:
    def __init__(self, row: int, index: int, value: str):
        self.row = row
        self.index = index
        self.value = value
        self.visited = set()
        self.energy_direct = None

    def next_step(self) -> list[tuple[str, int, int]]:
        match self.value:
            case '.':
                return [(self.energy_direct, self.row, self.index)]
            case '/':
                if self.energy_direct == '>':
                    return [('^', self.row, self.index)]
                elif self.energy_direct == '<':
                    return [('v', self.row, self.index)]
                elif self.energy_direct == '^':
                    return [('>', self.row, self.index)]
                else:
                    return [('<', self.row, self.index)]
            case '-':
                if self.energy_direct == '>':
                    return [('>', self.row, self.index)]
                elif self.energy_direct == '<':
                    return [('<', self.row, self.index)]
                else:
                    return [('<', self.row, self.index), ('>', self.row, self.index)]
            case '|':
                if self.energy_direct == 'v':
                    return [('v', self.row, self.index)]
                elif self.energy_direct == '^':
                    return [('^', self.row, self.index)]
                else:
                    return [('^', self.row, self.index), ('v', self.row, self.index)]
            case _:
                if self.energy_direct == '>':
                    return [('v', self.row, self.index)]
                elif self.energy_direct == '<':
                    return [('^', self.row, self.index)]
                elif self.energy_direct == '^':
                    return [('<', self.row, self.index)]
                else:
                    return [('>', self.row, self.index)]

    def __str__(self):
        if self.value == '.' and self.energy_direct:
            return f'{self.energy_direct:^3}'
        return f'{self.value:^3}'


def data_reader(path: str) -> list[list[Cell]]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    map_data = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            row.append(Cell(i, j, data[i][j]))
        map_data.append(row)
    return map_data


def print_map(data: list[list[Cell]], grid: bool = False):
    for row in data:
        [print(' # ' if (grid and cell.energy_direct) else cell, end='') for cell in row]
        print()


def movement(direct: str, x: int, y: int) -> tuple[int, int]:
    moves = {
        '>': (x, y + 1),
        '<': (x, y - 1),
        '^': (x - 1, y),
        'v': (x + 1, y)
    }
    return moves[direct]


def solution(data_map: list[list[Cell]]):
    result = 0
    data_map[0][0].energy_direct = '>'
    cell_path = [data_map[0][0]]
    while cell_path:
        cur_cell = cell_path.pop(0)
        for direction, row, index in cur_cell.next_step():
            row, index = movement(direction, row, index)
            if 0 <= row < len(data_map) and 0 <= index < len(data_map[row]):
                next_cell = data_map[row][index]
                if next_cell.value == '.' or next_cell.value in ['|', '-', '/', '\\'] and direction not in cur_cell.visited:
                    next_cell.energy_direct = direction
                    cell_path.append(next_cell)
                    cur_cell.visited.add(direction)
    for row in data_map:
        for cell in row:
            cur_cell = cell.energy_direct
            result += bool(cur_cell)
    return result


data = data_reader('input_data.txt')

print(solution(data))
print_map(data)
