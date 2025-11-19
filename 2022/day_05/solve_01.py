def read_data(path: str):
    with open(path, 'r') as file:
        result = []
        boxes = []
        for line in file.readlines():
            line = line.strip('\n')
            if line:
                boxes.append(line.replace(' ', '.'))
            else:
                result.append(boxes)
                boxes = []
        result.append(boxes)
    return result


def create_boxes(boxes_data: list[str]):
    boxes = {}
    idx = 1
    for line in zip(*boxes_data[:-1]):
        line = ''.join(line).replace('.', '').replace('[', '').replace(']', '')
        if line:
            boxes[idx] = list(line)[::-1]
            idx += 1
    return boxes


def create_moves(moves_data: list[str]):
    moves = []
    for line in moves_data:
        a, b, c = map(int, line.replace('move.', ' ').replace('.from.', ' ').replace('.to.', ' ').split())
        moves.append((a, b, c))
    return moves


def move_box(boxes: dict[int, list[str]], amount: int, idx_from: int, idx_to: int):
    box_at_home, box = boxes[idx_from][:-amount], boxes[idx_from][-amount:]
    boxes[idx_from] = box_at_home
    boxes[idx_to].extend(box)


def solution(path: str):
    boxes, moves = read_data(path)
    boxes = create_boxes(boxes)
    for amount, fr, t in create_moves(moves):
        move_box(boxes, amount, fr, t)
    result = ''
    for box in boxes.values():
        result += box.pop()
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
