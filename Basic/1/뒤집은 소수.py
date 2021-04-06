def reverse(x):
    val = str(x)
    val = val[-1:0:-1] + val[0]
    return int(val)


def isPrime_Best(n):
    if n < 2:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False
    b = round(n ** 0.5) + 1
    for i in range(3, b, 2):
        if n % i is 0:
            return False
    return True


def isPrime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())

arr = list(map(int, input().split()))
ans = []

for i in arr:
    tmp = reverse(i)
    if isPrime(tmp):
        ans.append(tmp)

print(ans)
