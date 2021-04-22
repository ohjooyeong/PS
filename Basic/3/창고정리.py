n = int(input())

arr = list(map(int, input().split()))
m = int(input())

for i in range(m):
    maxValue = max(arr)
    minValue = min(arr)
    arr[arr.index(maxValue)] -= 1
    arr[arr.index(minValue)] += 1

maxValue = max(arr)
minValue = min(arr)

print(maxValue - minValue)
