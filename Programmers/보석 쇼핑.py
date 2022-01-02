# 보석 쇼핑 67258


def checkValid(gems, section):
    for g in gems:
        if g in section:
            continue
        else:
            return False
    return True


def solution(gems):
    answer = []
    check_gem = list(set(gems))
    for i in range(len(gems)):
        for j in range(i, len(gems)):
            tmp_gem = gems[i : j + 1]
            if checkValid(check_gem, tmp_gem):
                answer.append([abs(i - j), i + 1, j + 1])
    answer.sort()
    answer = [answer[0][1], answer[0][2]]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

# def solution(gems):
#     answer = []
#     check_gem = list(set(gems))
#     lt = 0
#     rt = len(gems) - 1
#     while

#     return answer
