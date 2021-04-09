# 답안지 봤던 문제 다시 풀어봐야함!

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n // 2

for i in range(n):
    res += sum(arr[i][s : e + 1])
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

# for i in range(n):
#     for j in range(s, e + 1):
#         res += a[i][j]
#     if i < n // 2:
#         s -= 1
#         e += 1
#     else:
#         s += 1
#         e -= 1

print(res)
