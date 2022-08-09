n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[-1]
second = arr[-2]

ans = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        ans += first
        m -= 1
    if m == 0:
        break
    ans += second
    m -= 1

print(ans)
