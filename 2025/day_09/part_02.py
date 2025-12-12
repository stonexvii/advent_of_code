from collections import namedtuple

Square = namedtuple('Square', ('idx', 'row'))


def read_data(path: str):
    with open(path, 'r') as file:
        return [Square(*map(int, line.strip().split(','))) for line in file.readlines()]


def solution(path: str):
    square_data = read_data(path)
    squares = {}

    def get_middle(a_s: Square, b_s: Square):
        if a_s.idx == b_s.idx:
            min_row, max_row = sorted([a_s.row, b_s.row])
            return Square(a_s.idx, min_row + (max_row - min_row) // 2)
        else:
            min_idx, max_idx = sorted([a_s.idx, b_s.idx])
            return Square(min_idx + (max_idx - min_idx) // 2, a_s.row)

    def check_squares(min_row, max_row, min_idx, max_idx, squares_list):
        for square in squares_list:
            if min_row < square.row < max_row and min_idx < square.idx < max_idx:
                return True
        return False

    for a_square in square_data:
        for b_square in square_data:
            if a_square != b_square:
                area = (abs(a_square.row - b_square.row) + 1) * (abs(a_square.idx - b_square.idx) + 1)
                squares[area] = [a_square, b_square]

    for area, (a_square, b_square) in sorted(squares.items(), reverse=True):
        a_row, b_row = sorted([a_square.row, b_square.row])
        a_idx, b_idx = sorted([a_square.idx, b_square.idx])

        for i in range(len(square_data)):
            middle_square = get_middle(square_data[i - 1], square_data[i])
            if check_squares(a_row, b_row, a_idx, b_idx, [square_data[i - 1], middle_square, square_data[i]]):
                break
        else:
            return area


if __name__ == '__main__':
    print(solution('input_data.txt'))
