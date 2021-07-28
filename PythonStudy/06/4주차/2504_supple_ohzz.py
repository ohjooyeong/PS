# 괄호의 값 2504 백준
import sys

string = input()
stack = []
res = 0

for s in string:
    if s == ")":
        tmp = 0
        while stack:
            top = stack.pop()
            if top == "(":
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * tmp)
                break
            elif top == "[":
                print(0)
                sys.exit(0)
            else:
                tmp += top
    elif s == "]":
        tmp = 0
        while stack:
            top = stack.pop()
            if top == "[":
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            elif top == "(":
                print(0)
                sys.exit(0)
            else:
                tmp += top
    else:
        stack.append(s)

for i in stack:
    if i == "(" or i == "[":
        print(0)
        sys.exit(0)
    else:
        res += i
print(res)