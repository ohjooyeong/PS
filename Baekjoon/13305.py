# 주유소 13305 백준

n = int(input())

dis = list(map(int, input().split()))
oilCost = list(map(int, input().split()))

minOilCost = oilCost[0]
sum = 0

for i in range(n - 1):
    if minOilCost > oilCost[i]:
        minOilCost = oilCost[i]
    sum += minOilCost * dis[i]

print(sum)
