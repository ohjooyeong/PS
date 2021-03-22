# 완주하지 못한 선수


def solution(p, c):
    p.sort()
    c.sort()
    for i in range(len(c)):
        if p[i] != c[i]:
            return p[i]
    return p[-1]


# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
# print(solution(participant, completion))
