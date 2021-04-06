def digit_sum(x):
    sum = 0
    while x:
        sum += x % 10
        x = x // 10
    return sum


n = int(input())

arr = list(map(int, input().split()))
max = 0

for i in arr:
    if digit_sum(i) > max:
        max = digit_sum(i)
        ans = i

print(ans)
