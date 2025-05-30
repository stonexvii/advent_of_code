def print_table(table, direct=1):
    for row in table:
        print(' '.join([ch for ch in row][::direct]))

def turn_table(data: list[str]) -> list[str]:
    return [''.join(row) for row in list(zip(*[row for row in data[::-1]]))]


def data_reader(path: str) -> list[str]:
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    data = list(zip(*data))
    return [''.join(row) for row in data]


def solution(data_table: list[str]) -> list[str]:
    result = []
    print_table(data_table)

    def roll_down(row_slice: str):
        stone_count = row_slice.count('O')
        return 'O' * stone_count + '.' * (len(row_slice) - stone_count)

    for row in data_table:
        final_row = ''
        for str_slice in row.split('#'):
            if str_slice:
                final_row += roll_down(str_slice) + '#'
            else:
                final_row += '#'
        result.append(final_row[:-1])
    return result


table = data_reader('test_data.txt')
for i in range(4):
    table = solution(table)
    table = turn_table(table)
    print()
