# 백준 손익분기점

import sys

a, b, c = map(int, sys.stdin.readline().split())
n = 0
if b < c:
    n = a // (c - b) + 1
    print(n)
else:
    print(-1)
