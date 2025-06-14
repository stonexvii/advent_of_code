def read_data(path: str) -> tuple[list[str], str]:
    with open(path, 'r') as file:
        *rules, _, molecule = [line.strip().split(' => ') if '=>' in line else line.strip() for line in
                               file.readlines()]
    return rules, molecule


def solution(path: str):
    rules, molecule = read_data(path)
    count = 0
    while molecule != 'e':
        for rule in rules:
            if molecule.count(rule[1]):
                molecule = molecule.replace(rule[1], rule[0], 1)
                count += 1
                break
    return count


if __name__ == '__main__':
    print(solution('input_data.txt'))
