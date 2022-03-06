# 문자열 압축 60057
def solution(s):
    answer = 1001
    n = len(s)

    if n == 1:
        return n

    for i in range(1, n // 2 + 1):
        lt = 0
        rt = i
        cnt = 1
        prev = s[lt:rt]
        tmp = ""
        while rt <= n + i:
            lt = rt
            rt = lt + i
            next = s[lt:rt]
            if prev == next:
                cnt += 1
            else:
                if cnt > 1:
                    tmp += str(cnt) + prev
                    cnt = 1
                else:
                    tmp += prev
            prev = next

        if len(tmp) < answer:
            answer = len(tmp)
    return answer


# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
