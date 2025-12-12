from itertools import combinations_with_replacement, product, chain



def read_data(path: str):
    with open(path, 'r') as file:
        while line := file.readline():
            lamps, data = line.strip().split(' ', 1)
            lamps = list(lamps[1:-1])
            buttons, _ = data.rsplit(' ', 1)
            buttons = buttons.replace('(', '').replace(')', '').split()
            buttons = [tuple(map(int, button.split(','))) for button in buttons]
            yield lamps, buttons


def switch(line: list[str], buttons: tuple[tuple[int, ...]]):
    for button in buttons:
        empty_line = ['.'] * len(line)
        pressed = []
        for press in button:
            # print(empty_line)
            empty_line[press] = '#' if empty_line[press] == '.' else '.'
            pressed.append(button)
            if empty_line == line:
                print(empty_line, line)
                print(pressed)
                return True


def solution(path: str):
    for lamps, buttons in read_data(path):
        for combo in chain(*[product(buttons, repeat=i) for i in range(1, len(buttons)+1)]):
            if switch(lamps, combo):
                print('FIND')
                break


if __name__ == '__main__':
    solution('test_data.txt')
    # a = [1,2,3]
    # for line in :
    #     print(line)