n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

lt = 1
rt = max(arr)

res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 1
    prev = arr[0]
    for i in range(1, n):
        if arr[i] - prev >= mid:
            cnt += 1
            prev = arr[i]
    if cnt >= c:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)
