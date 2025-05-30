from solve_01 import check_hash, data_reader

# puzzle_data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
puzzle_data = data_reader('input_data.txt')

def solution(lens_data: str):
    result = 0
    boxes = [{} for _ in range(256)]
    for lens in lens_data.split(','):
        if '=' in lens:
            index, number = lens.split('=')
            boxes[check_hash(index)][index] = number
        else:
            index = lens[:-1]
            for box in boxes[check_hash(index)]:
                if index in box:
                    boxes[check_hash(index)].pop(box)
                    break
    for i, box in enumerate(boxes,1):
        count = 1
        for lens, number in box.items():
            result += count * i * int(number)
            count += 1
    return result


print(solution(puzzle_data))

