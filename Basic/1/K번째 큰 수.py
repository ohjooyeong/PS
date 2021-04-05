n, k = map(int, input().split())
arr = list(map(int, input().split()))

sumArr = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            sumArr.add(arr[i] + arr[j] + arr[m])
sumArr = list(sumArr)
sumArr.sort(reverse=True)

print(sumArr[k - 1])
