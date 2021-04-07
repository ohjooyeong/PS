n = int(input())
arr = []

for i in range(n):
    tmp = input()
    arr.append(tmp)

k = 0
for s in arr:
    k += 1
    s = s.upper()
    if s == (s[::-1]):
        print(f"{k} YES")
    else:
        print(f"{k} NO")
