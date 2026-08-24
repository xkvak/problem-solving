"""백준 10868. 최솟값"""

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


INF = 10**18


def init_tree(arr: list):
    size = 1 << (len(arr) - 1).bit_length()
    tree = [INF] * (size * 2)

    for i, _ in enumerate(arr):
        tree[size + i] = arr[i]

    for i in range(size - 1, 0, -1):
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])

    return tree, size


def query(tree, size, left, right):
    left += size - 1
    right += size - 1
    result = INF

    while left <= right:
        if left % 2 == 1:
            result = min(result, tree[left])
            left += 1
        if right % 2 == 0:
            result = min(result, tree[right])
            right -= 1
        left //= 2
        right //= 2

    return result


def main():
    n, m = map(int, sys_input().split())
    arr = [int(sys_input()) for _ in range(n)]
    tree, size = init_tree(arr)

    for _ in range(m):
        a, b = map(int, sys_input().split())
        print(query(tree, size, a, b))


if __name__ == "__main__":
    main()
