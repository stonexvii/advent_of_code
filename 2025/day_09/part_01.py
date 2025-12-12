from collections import namedtuple

Square = namedtuple('Square', ('idx', 'row'))


def read_data(path: str):
    with open(path, 'r') as file:
        return [Square(*map(int, line.strip().split(','))) for line in file.readlines()]


def solution(path: str):
    square_data = read_data(path)
    squares = {}
    maximum_area, result_squares = 0, []
    for a_square in square_data:
        squares[a_square] = {}
        for b_square in square_data:
            if a_square != b_square:
                area = (abs(a_square.row - b_square.row) + 1) * (abs(a_square.idx - b_square.idx) + 1)
                squares[a_square][b_square] = area
                if maximum_area < area:
                    maximum_area = area
                    result_squares = [a_square, b_square]
    return maximum_area, result_squares

    # for line in squares.items():
    #     print(line)


if __name__ == '__main__':
    print(solution('input_data.txt'))
