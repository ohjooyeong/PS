n, m = map(int, input().split())

ans = 0

for i in range(n):
    arr = list(map(int, input().split()))
    min_value = min(arr)
    ans = max(min_value, ans)

print(ans)
