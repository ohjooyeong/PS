n, m = map(int, input().split())

arr = list(map(int, input().split()))

print(len(arr))

arr.sort()

lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if arr[mid] == m:
        break
    elif arr[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1

print(mid + 1)
