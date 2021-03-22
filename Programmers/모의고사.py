# 모의 고사


def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    z, x, c = 0, 0, 0
    answer = []
    for i in range(len(answers)):
        if p1[z] == answers[i]:
            score[0] += 1
        if p2[x] == answers[i]:
            score[1] += 1
        if p3[c] == answers[i]:
            score[2] += 1
        z += 1
        x += 1
        c += 1
        if z == len(p1):
            z = 0
        if x == len(p2):
            x = 0
        if c == len(p3):
            c = 0
    for i, x in enumerate(score):
        if max(score) == x:
            answer.append(i + 1)
    return answer


print(solution([1, 2, 3, 4, 5]))
