n = int(input())

arr = list(map(int, input().split()))

seq = [0] * n
for i in range(n):
    for j in range(n):
        if arr[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            arr[i] -= 1
for x in seq:
    print(x, end=" ")
# arr = arr[::-1]
# ans = []
# for x in a:
#     ans.insert(x, n)
#     n -= 1
# print(ans)
