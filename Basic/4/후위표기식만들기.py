# 답안지 보고 품 다시 풀어봐야함

a = input()
stack = []
res = ""
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":

            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)
