"""백준 1561. 놀이 공원"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n, m, arr: list):
    min_time, max_time = 0, max(arr) * n
    while min_time < max_time:
        time = (min_time + max_time) // 2
        boarded_cnt = m + sum(time // ride for ride in arr)
        if n <= boarded_cnt:
            max_time = time
        else:
            min_time = time + 1

    boarded_cnt = m + sum((min_time - 1) // ride for ride in arr)
    remain_cnt = n - boarded_cnt
    for idx, num in enumerate(arr, 1):
        if min_time % num == 0:
            remain_cnt -= 1
        if remain_cnt == 0:
            return idx

    return None


def main():
    n, m = map(int, sys_input().split())
    arr = list(map(int, sys_input().split()))
    print(solve(n, m, arr))


if __name__ == "__main__":
    main()
