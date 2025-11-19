def read_data(path: str):
    with open(path, 'r') as file:
        return file.read()


def solution(path: str):
    data = read_data(path)
    elves = []
    calories = 0
    for line in data.split('\n'):
        if line:
            calories += int(line.strip())
        else:
            elves.append(calories)
            calories = 0
    elves.sort(reverse=True)
    return sum(elves[:3])


if __name__ == '__main__':
    print(solution('input_data.txt'))
