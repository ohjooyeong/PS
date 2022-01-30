# 양궁대회 프로그래머스

from itertools import *


def last_comp(x, y):
    return x[::-1] > y[::-1]


def solution(n, info):
    answer = [-1]
    max_score = 0
    for comb in combinations_with_replacement(range(11), n):
        score = 0
        arrow = [0] * 11

        for c in comb:
            arrow[c] += 1

        for i in range(11):
            if info[i] < arrow[i]:
                score += 10 - i
            elif info[i] != 0:
                score -= 10 - i

        if score <= 0:
            continue

        if score >= max_score:
            if max_score == score:
                if not last_comp(answer, arrow) and len(answer) > 1:
                    answer = arrow[:]
            else:
                answer = arrow[:]
            max_score = score

    if answer[0] == -1:
        return [-1]
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
