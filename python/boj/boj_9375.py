import sys

sys_input = sys.stdin.readline
for _ in range(int(sys_input())):
    clothes_type = {}
    for _ in range(int(sys_input())):
        _, type = sys_input().strip().split()
        clothes_type[type] = clothes_type.get(type, 1) + 1

    result = 1
    for _, value in clothes_type.items():
        result *= value
    print(result - 1)
