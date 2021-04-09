n, m = map(int, input().split())

arr = list(map(int, input().split()))

lt = 0
rt = 1
cnt = 0


while True:
    if m > sum(arr[lt:rt]):
        if rt < n:
            rt += 1
        else:
            break
    elif m == sum(arr[lt:rt]):
        cnt += 1
        lt += 1
    else:
        lt += 1

# while True:
#     if tot < m:
#         if rt < n:
#             tot += arr[rt]
#             rt += 1
#         else:
#             break
#     elif tot == m:
#         cnt += 1
#         tot -= arr[lt]
#         lt += 1
#     else:
#         tot -= arr[lt]
#         lt += 1

print(cnt)
