arr = [i + 1 for i in range(20)]

for _ in range(10):
    ai, bi = map(int, input().split())
    part = bi - ai + 1
    cnt = 0
    for j in range(ai - 1, ai - 1 + (part // 2)):
        arr[j], arr[bi - 1 - cnt] = arr[bi - 1 - cnt], arr[j]
        cnt += 1
    # for j in range(part // 2):
    #     a[ai + j], a[bi - j] = a[ai - j], a[ai + j]
print(arr)
