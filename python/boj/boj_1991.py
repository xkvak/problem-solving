import sys

sys_input = sys.stdin.readline
n = int(sys_input())
a = [[] for _ in range(26)]
for _ in range(n):
    parent, left, right = map(lambda n1: ord(n1) - 65, sys_input().split())
    a[parent].append(left)
    a[parent].append(right)

result = [[] for _ in range(3)]


def preorder(curr, a):
    if curr < 0:
        return
    result[0].append(chr(curr + 65))
    preorder(a[curr][0], a)
    preorder(a[curr][1], a)


def inorder(curr, a):
    if curr < 0:
        return
    inorder(a[curr][0], a)
    result[1].append(chr(curr + 65))
    inorder(a[curr][1], a)


def postorder(curr, a):
    if curr < 0:
        return
    postorder(a[curr][0], a)
    postorder(a[curr][1], a)
    result[2].append(chr(curr + 65))


preorder(0, a)
inorder(0, a)
postorder(0, a)

for r in result:
    print("".join(r))
