from collections import namedtuple


class Password:
    def __init__(self, line: str):
        rule, password = line.strip().split(': ')
        amount, letter = rule.split()
        min_amount, max_amount = map(int, amount.split('-'))
        self.min = min_amount
        self.max = max_amount
        self.letter = letter
        self.password = password

    def check(self):
        return self.min <= self.password.count(self.letter) <= self.max

    def check_position(self):
        first = self.password[self.min - 1] == self.letter
        second = self.password[self.max - 1] == self.letter
        return len({first, second}) == 2


def read_data(path: str):
    with open(path, 'r') as file:
        while line := file.readline():
            yield Password(line)


def solution(path: str):
    return sum([1 for password in read_data(path) if password.check_position()])


if __name__ == '__main__':
    print(solution('input_data.txt'))
