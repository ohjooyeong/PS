import math

N = int(input())
arr = list(map(int, input().split()))

avg = math.ceil(sum(arr) / N)
# avg = round(sum(arr) / N)
tmp = 100
ans = 0

for i in range(N):
    if abs(arr[i] - avg) <= tmp:
        tmp = abs(arr[i] - avg)
        if ans < arr[i]:
            ans = arr[i]
            seq = i + 1

# for idx, x in enumerate(a):
#     tmp = abs(x - avg)
#     if tmp < min:
#         min = tmp:
#         score = x
#         res = idx = 1
#     elif tmp == min:
#         if x > score:
#             score = x
#             res = idx + 1

print(f"{avg} {seq}")
