def read_data(path: str):
    with open(path, 'r') as file:
        data = [x.strip().split() for x in file.readlines()]
    return data


class Game:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 1
        self.d = 0

    def move(self, *args):
        if args[0] == 'cpy':
            self.__setattr__(args[2], int(args[1]) if args[1].isdigit() else self.__getattribute__(args[1]))
        elif args[0] == 'inc':
            self.__setattr__(args[1], self.__getattribute__(args[1]) + 1)
        elif args[0] == 'dec':
            self.__setattr__(args[1], self.__getattribute__(args[1]) - 1)
        else:
            if args[1].isdigit() and int(args[1]) or self.__getattribute__(args[1]):
                return int(args[2])
        return 1

    def __str__(self):
        return str(self.__dict__)


def solution(path: str):
    data_map = read_data(path)
    idx = 0
    game = Game()
    while idx < len(data_map):
        idx += game.move(*data_map[idx])
    return game


if __name__ == '__main__':
    print(solution('input_data.txt'))
