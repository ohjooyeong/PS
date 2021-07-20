# 주유소 13305 백준

n = int(input())

dis = list(map(int, input().split()))
oil = list(map(int, input().split()))

minOil = oil[0]
sum = 0

for i in range(n - 1):
    if minOil > oil[i]:
        minOil = oil[i]
    sum += minOil * dis[i]

print(sum)
