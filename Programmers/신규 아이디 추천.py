# 신규 아이디 추천

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isdigit() or i == "-" or i == "." or i.isalpha() or i == "_":
            answer += i
    k = 0
    while True:
        if len(answer) == k + 1:
            break
        if answer[k] == "." and answer[k + 1] == ".":
            answer = answer.replace("..", ".")
            k = 0
        else:
            k += 1
    if len(answer) > 0 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == ".":
        answer = answer[0:-1]
    if answer == "":
        answer += "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[0:-1]
    if len(answer) <= 2:
        last = answer[-1]
        for i in range(3):
            answer += last
            if len(answer) == 3:
                break
    return answer

# new_id = "...!@BaT#*..y.abcdefghijklm"
# print(solution(new_id))
