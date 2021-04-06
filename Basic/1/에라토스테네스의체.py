def isPrimeList(value):
    primeCheck = [0] * (value + 1)
    ans = 0
    for i in range(2, (value // 2) + 1):
        if primeCheck[i] == 0:
            for j in range(i + i, value + 1, i):
                primeCheck[j] = 1
    for i in range(2, value + 1):
        if primeCheck[i] == 0:
            ans += 1
    return ans


n = int(input())

print(isPrimeList(n))
