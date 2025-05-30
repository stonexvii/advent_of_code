
class Deer:
    def __init__(self, data: str):
        data = data.split()
        self.speed = int(data[3])
        self.duration = int(data[6])
        self.rest = int(data[13])
        self.distance = 0
        self.elapsed_time = 0

    def run_deer_run(self, stop_time: int):
        while self.elapsed_time <= stop_time:
            for second in range(self.duration):
                self.distance += self.speed
                self.elapsed_time += 1
                if self.elapsed_time >= stop_time:
                    return self.distance
            self.elapsed_time += self.rest


def read_data(path: str) -> list[Deer]:
    deer_list = []
    with open(path, 'r') as file:
        for line in file.readlines():
            deer_list.append(Deer(line))
    return deer_list


def solution(path: str, time: int) -> int:
    deer_list = read_data(path)
    for deer in deer_list:
        deer.run_deer_run(time)
    return max(deer_list, key=lambda x: x.distance).distance


if __name__ == '__main__':
    print(solution('input_data.txt', 2503))
