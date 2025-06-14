def read_data(path: str) -> tuple[list[str], str]:
    with open(path, 'r') as file:
        *rules, _, molecule = [line.strip().split(' => ') if '=>' in line else line.strip() for line in
                               file.readlines()]
    return rules, molecule


def solution(path: str):
    rules, molecule = read_data(path)
    molecules = set()
    for rule in rules:
        idx = 0
        for _ in range(molecule.count(rule[0])):
            start_molecule, rest_molecule = molecule[:idx], molecule[idx:]
            new_molecule = start_molecule + rest_molecule.replace(rule[0], rule[1], 1)
            molecules.add(new_molecule)
            idx += molecule[idx:].index(rule[0]) + len(rule[0])
    return len(molecules)


if __name__ == '__main__':
    print(solution('input_data.txt'))
