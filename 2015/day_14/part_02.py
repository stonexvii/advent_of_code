class Deer:
    def __init__(self, data: str):
        data = data.split()
        self.speed = int(data[3])
        self.duration = int(data[6])
        self.rest = int(data[13])
        self.score = 0
        self.distance = 0
        self.elapsed_time = 0
        self.run = True
        self.time_to_rest = self.duration
        self.rest_time = 0

    def next_second(self):
        if self.run:
            self.distance += self.speed
            self.time_to_rest -= 1
            if not self.time_to_rest:
                self.time_to_rest = self.duration
                self.run = False
        else:
            self.rest_time += 1
            if self.rest_time == self.rest:
                self.rest_time = 0
                self.run = True


def read_data(path: str) -> list[Deer]:
    deer_list = []
    with open(path, 'r') as file:
        for line in file.readlines():
            deer_list.append(Deer(line))
    return deer_list


def solution(path: str, time: int) -> int:
    deer_list = read_data(path)
    max_position = 0
    for _ in range(time):
        for deer in deer_list:
            deer.next_second()
            if deer.distance > max_position:
                max_position = deer.distance
        for deer in deer_list:
            if deer.distance == max_position:
                deer.score += 1
    return max(deer_list, key=lambda x: x.score).score


if __name__ == '__main__':
    print(solution('input_data.txt', 2503))
