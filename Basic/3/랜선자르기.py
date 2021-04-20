k, n = map(int, input().split())

arr = []

for i in range(k):
    arr.append(int(input()))

# cnt = 10000000000000000
# res = 1
# while True:
#     cnt = 0
#     for i in range(k):
#         cnt += arr[i] // res
#     if cnt < n:
#         break
#     res += 1


def Count(length):
    cnt = 0
    for x in arr:
        cnt += x // length
    return cnt


lt = 1
rt = max(arr)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
