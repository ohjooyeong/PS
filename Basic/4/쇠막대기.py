# 답안지 보고 품 다시 봐야함

pole = input()

stack = []

ans = 0
for i in range(len(pole)):
    if pole[i] == ")":
        if pole[i - 1] == "(":
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
    else:
        stack.append(pole[i])

print(ans)
