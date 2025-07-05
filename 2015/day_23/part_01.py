class Operation:
    registers = {
        'a': 0,
        'b': 0,
    }

    def __init__(self, operator: str, register: str | None = None, value: str | None = None):
        self.operator = operator
        self.register = register
        if value:
            self.value = int(value[1:]) if value.startswith('+') else -int(value[1:])
        else:
            self.value = None

    def run(self):
        if self.operator == 'inc':
            Operation.registers[self.register] += 1
        elif self.operator == 'tpl':
            Operation.registers[self.register] *= 3
        elif self.operator == 'jmp':
            return self.value
        elif self.operator == 'jie':
            if not Operation.registers[self.register] % 2:
                return self.value
        elif self.operator == 'jio':
            if Operation.registers[self.register] == 1:
                return self.value
        elif self.operator == 'hlf':
            Operation.registers[self.register] //= 2
        return 1

    def __repr__(self):
        return f'{self.operator} {self.register} {self.value}'


def read_data(path: str):
    with open(path, 'r') as file:
        program = []
        for line in file.readlines():
            operator, register, value = line.strip().split(' ', 1) + [None]

            if operator in ('jie', 'jio'):
                register, value = register.split(', ')
            elif operator == 'jmp':
                value = register
                register = None
            program.append(Operation(operator, register, value))
    return program


def solution(path: str):
    program = read_data(path)
    idx = 0
    while idx < len(program):
        amount = program[idx].run()
        idx += amount
        print(Operation.registers)


if __name__ == '__main__':
    solution('input_data.txt')
