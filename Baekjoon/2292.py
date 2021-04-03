# 백준 벌집

n = int(input())

count = 0
sum = 1
while True:
    sum += 1 * 6 * count
    if sum >= n:
        print(count + 1)
        break
    count += 1
