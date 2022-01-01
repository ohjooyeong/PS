# 수식최대화 67257

from itertools import permutations


def calc(x, y, op):
    if op == "+":
        return x + y
    elif op == "*":
        return x * y
    else:
        return x - y


def sol(num, opr, oprs):
    num = num[:]
    opr = opr[:]
    for op in oprs:
        while op in opr:
            idx = opr.index(op)  # 각 연산자가 있는 index 값을 찾음
            num[idx] = calc(
                num[idx], num[idx + 1], op
            )  # 숫자 배열에서 연산자 index, 연산자 + 1 index 인곳이 각 숫자를 연산할 곳임
            del num[idx + 1]
            del opr[idx]

    return abs(num[0])


def solution(expression):
    answer = []
    # 6가지 operation 정의
    operations = list(permutations(["*", "+", "-"], 3))
    opr = []
    nums = list(
        map(int, expression.replace("-", " ").replace("+", " ").replace("*", " ").split(" "))
    )
    for s in expression:
        if s == "-" or s == "*" or s == "+":
            opr.append(s)

    while operations:
        answer.append(sol(nums, opr, list(operations.pop())))

    return max(answer)
