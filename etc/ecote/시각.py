h = int(input())

ans = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                ans += 1

print(ans)
