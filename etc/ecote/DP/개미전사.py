n = int(input())
meal = list(map(int, input().split()))

d = [0] * 100

d[0] = meal[0]
d[1] = max(meal[0], meal[1])

for i in range(2, n):
    d[i] = max(d[i - 1], meal[i] + d[i - 2])

print(d[n - 1])

print(d)
