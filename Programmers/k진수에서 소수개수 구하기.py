# k진수에서 소수 개수 구하기


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def base_change(n, k):
    rev_base = ""

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n, k):
    answer = 0
    base = base_change(n, k)
    nums = base.split("0")
    for num in nums:
        if num:
            num = int(num)
            if is_prime(num):
                answer += 1
    return answer


print(solution(437674, 3))
print(solution(110011, 10))
