from collections import namedtuple

Create = namedtuple('Create', ['x', 'y'])
Rotate = namedtuple('Rotate', ['direct', 'index', 'amount'])


def read_data(path: str):
    operations = []
    with open(path, 'r') as file:
        for line in file:
            operation, value = line.strip().split(' ', 1)
            if operation == 'rect':
                operations.append(Create(*map(int, value.split('x'))))
            else:
                direct, data = value.split(' ', 1)
                index, amount = map(int, data[2:].split(' by '))
                operations.append(Rotate(direct, index, amount))

    return operations


class Matrix:
    def __init__(self, columns: int, rows: int):
        self.matrix = [[' ' for _ in range(rows)] for _ in range(columns)]

    def swap(self):
        self.matrix = list(map(lambda x: list(x), zip(*self.matrix)))

    def create_rect(self, rows: int, columns: int):
        for i in range(rows):
            for k in range(columns):
                self.matrix[k][i] = '*'

    def rotate(self, direct: str, index: int, amount: int):
        if direct == 'column':
            self.swap()
        for _ in range(amount):
            self.matrix[index].insert(0, self.matrix[index].pop())
        if direct == 'column':
            self.swap()

    def show(self):
        print()
        print(*self.matrix, sep='\n')
        print()

    def decode(self):
        print(*map(lambda x: ''.join(x), self.matrix), sep='\n')

    def total_lights(self):
        return sum(map(sum, self.matrix))


def solution(path: str, rows: int, columns: int):
    matrix = Matrix(rows, columns)
    operations = read_data(path)
    for operation in operations:
        if isinstance(operation, Create):
            matrix.create_rect(operation.x, operation.y)
        else:
            matrix.rotate(operation.direct, operation.index, operation.amount)
    matrix.decode()


if __name__ == '__main__':
    print(solution('input_data.txt', 6, 50))
