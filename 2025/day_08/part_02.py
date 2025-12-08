from collections import namedtuple

# from itertools import chain

Box = namedtuple('Box', ('x', 'y', 'z'))


def read_data(path: str):
    data = {}
    with open(path, 'r') as file:
        for idx, line in enumerate(file.readlines(), 1):
            data[idx] = Box(*map(int, line.strip().split(',')))
    return data


def solution(path: str):
    boxes = read_data(path)
    min_distance = []
    for a_box, c in boxes.items():
        for b_box, oc in boxes.items():
            if a_box != b_box:
                distance = (c.x - oc.x) ** 2 + (c.y - oc.y) ** 2 + (c.z - oc.z) ** 2
                key = tuple(sorted([a_box, b_box]))
                min_distance.append((distance, key))
    min_distance = list(map(lambda x: x[1], sorted(set(min_distance))))
    chains = {}
    for a_box, b_box in min_distance:
        a_chain, b_chain = {a_box}, {b_box}
        if chains:
            for idx, chain in chains.items():
                if a_chain.intersection(chain):
                    a_chain = chains.pop(idx)
                    break
            for idx, chain in chains.items():
                if b_chain.intersection(chain):
                    b_chain = chains.pop(idx)
                    break
        idx = max(chains) + 1 if chains else 1
        chains[idx] = a_chain.union(b_chain)
        if len(max(chains.values(), key=len)) == len(boxes):
            return boxes[a_box].x * boxes[b_box].x


if __name__ == '__main__':
    print(solution('input_data.txt'))
