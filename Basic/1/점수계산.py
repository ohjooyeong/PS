n = int(input())
cnt = 0
arr = list(map(int, input().split()))
score = [0] * n

for i in range(n):
    if arr[i] == 1:
        cnt += 1
        score[i] = cnt
    else:
        cnt = 0

print(sum(score))
