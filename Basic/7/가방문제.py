n, k = map(int, input().split())

dy = [0] * (k + 1)

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(w, k + 1):
        dy[i] = max(dy[i], dy[i - w] + v)

print(dy[-1])
