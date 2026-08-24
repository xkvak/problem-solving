from bisect import bisect_right
import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def a():
    n = int(sys_input())
    width, height = 4 * n + 2, 2 * n

    ans = [[[""] for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            ans[i][i] = "*"
            if i < n:
                ans[i][height + n - i] = "*"
                ans[i][height + n + i + 2] = "*"
            else:
                ans[i][height - n + i + 1] = "*"
                ans[i][height - n + i + 1 + height - i + height - i] = "*"

    ans.reverse()
    for data in ans:
        print("".join(x if isinstance(x, str) else " " for x in data))


def b():
    t = int(sys_input())
    for _ in range(t):
        n = int(sys_input())
        arr = list(list(map(int, sys_input().split())) for _ in range(n))
        ans = "YES"
        (
            max_a,
            max_b,
            max_c,
        ) = (
            0,
            0,
            0,
        )
        for i, (a, b, c, p) in enumerate(arr):
            max_a = max(a, max_a)
            max_b = max(b, max_b)
            max_c = max(c, max_c)
            if p <= max_a + max_b + max_c + i:
                ans = "NO"
                break
        print(ans)


def c():
    n, d = map(int, sys_input().split())
    ans = 0
    arr = []
    for i in range(n):
        t, a, b = map(int, sys_input().split())
        arr.append((t, a, b, i))
        ans = max(ans, a + b)

    by_times = sorted((t, b, i) for t, _, b, i in arr)
    times = [t for t, _, _ in by_times]

    best, second = [], []
    best_b, best_b_idx = -1, -1
    second_b, second_b_idx = -1, -1
    for _, b, i in by_times:
        if best_b < b:
            second_b, second_b_idx = best_b, best_b_idx
            best_b, best_b_idx = b, i
        elif second_b < b:
            second_b, second_b_idx = b, i

        best.append((best_b, best_b_idx))
        second.append((second_b, second_b_idx))

    for t, a, _, idx in arr:
        remain = d - t
        pos = bisect_right(times, remain) - 1
        if pos < 0:
            continue

        b, b_idx = best[pos]
        if b_idx == idx:
            b, b_idx = second[pos]
        if b_idx != -1:
            ans = max(ans, a + b)
    print(ans)


def j():
    print("Good Bye, BOJ!")


if __name__ == "__main__":
    c()
