"""2026 musinsa rookie 1차 문제"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


class Brand:
    size_measurements: dict[str, list[int]]

    def __init__(self, sizes: list):
        self.size_measurements: dict[str, list[int]] = {}

        for s in sizes:
            name = str(s[0])
            s = list(map(int, s[1:]))
            self.size_measurements[name] = s

    def check(self, h, c, w):
        h_size, c_size, w_size = [], [], []
        for size, measurement in self.size_measurements.items():
            if measurement[0] <= h <= measurement[1]:
                h_size.append(size)
            if measurement[2] <= c <= measurement[3]:
                c_size.append(size)
            if measurement[4] <= w <= measurement[5]:
                w_size.append(size)

        for size in self.size_measurements:
            if size in h_size and size in c_size and size in w_size:
                return size

        min_measurement = next(iter(self.size_measurements.values()))
        max_measurement = next(reversed(self.size_measurements.values()))
        if h > max_measurement[1] and c > max_measurement[3] and w > max_measurement[5]:
            return "UP"
        if h < min_measurement[0] and c < min_measurement[2] and w < min_measurement[4]:
            return "DOWN"
        return "MISMATCH"


def main():
    brands: dict[str, Brand] = {}
    b, q = map(int, sys_input().split(","))
    for _ in range(b):
        s, n = tuple(sys_input().split(","))
        sizes = list(sys_input().split(",") for _ in range(int(n)))
        brands[s] = Brand(sizes)

    for _ in range(q):
        s, h, c, w = sys_input().split(",")
        if s in brands:
            print(f"{s},{brands[s].check(int(h), int(c), int(w))}")
        else:
            print(f"{s},UNKNOWN")


if __name__ == "__main__":
    main()
