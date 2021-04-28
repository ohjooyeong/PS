# 답안지 보고 품 다시 봐야함

nums, cnt = map(int, input().split())
nums = list(map(int, str(nums)))

stack = []

for i in nums:
    while stack and i > stack[-1] and cnt > 0:
        stack.pop()
        cnt -= 1
    stack.append(int(i))

while cnt:
    stack.pop()
    cnt -= 1

ans = "".join(map(str, stack))
print(ans)
