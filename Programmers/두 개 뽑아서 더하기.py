"https://programmers.co.kr/learn/courses/30/lessons/68644"

# 두개 뽑아서 더하기
def solution(numbers):
    answer = []
    res = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            res.add(numbers[i] + numbers[j])
    answer = list(res)
    answer.sort()
    return answer


# print(solution([2,1,3,4,1]))
