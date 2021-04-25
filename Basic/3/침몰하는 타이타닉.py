n, m = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
arr.sort()
while arr:
    if len(arr) > 1:
        tmp = arr[0] + arr[-1]
    else:
        tmp = arr[0]
    if tmp > m:
        cnt += 1
        arr.pop()
    else:
        cnt += 1
        if len(arr) > 1:
            arr.pop(0)
            arr.pop()
        else:
            arr.pop()

print(cnt)
