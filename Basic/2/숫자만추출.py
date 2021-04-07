string = input()
ans = ""

for i in string:
    if i.isalpha():
        continue
    ans += i
ans = int(ans)

res = []
for i in range(1, ans + 1):
    if ans % i == 0:
        res.append(i)

print(ans)
print(len(res))
