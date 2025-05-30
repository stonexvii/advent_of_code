from itertools import permutations


def read_data(path: str) -> dict[str, dict[str, int]]:
    result = {}
    with open(path, 'r') as file:
        for line in file.readlines():
            host, _, sign, value, *_, client = line[:-2].split()
            result.setdefault(host, {})
            result[host][client] = int(value) * (-1) ** (sign == 'lose')
    return result


def solution(path: str):
    guests = read_data(path)
    for key, value in guests.items():
        guests[key]['me'] = 0
    guests['me'] = dict.fromkeys(guests, 0)
    combo_guests = list(permutations(guests, len(guests)))
    happiness_list = []
    for combo in combo_guests:
        option = []
        for idx, guest in enumerate(combo):
            next_guest = combo[(idx + 1) % len(combo)]
            option.append(guests[guest][next_guest] + guests[next_guest][guest])
        happiness_list.append(sum(option))

    return max(happiness_list)


if __name__ == '__main__':
    print(solution('input_data.txt'))
