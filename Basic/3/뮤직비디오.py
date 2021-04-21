n, m = map(int, input().split())

video = list(map(int, input().split()))

lt = max(video)
rt = sum(video)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    tmp = 0
    cnt = 1
    for i in video:
        tmp += i
        if tmp > mid:
            cnt += 1
            tmp = i
            print(mid)
    if cnt <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
