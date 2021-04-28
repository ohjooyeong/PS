a = input()

stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        tmp = 0
        if x == "+":
            tmp += stack.pop() + stack.pop()
        elif x == "-":
            b = stack.pop()
            a = stack.pop()
            tmp += a - b
        elif x == "*":
            tmp += stack.pop() * stack.pop()
        elif x == "/":
            b = stack.pop()
            a = stack.pop()
            tmp += a / b
        stack.append(tmp)

print(stack[0])
