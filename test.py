def solution(n):
    answer = 18
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    for i in range(3, n):
        for j in range(i - 1, 0, -1):
            dp[i] = max(dp[5 - j] * dp[j], dp[i])
            print(dp[i], j)
    answer = dp[n]
    return answer


print(solution(8))
