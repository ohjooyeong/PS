n = int(input())

meeting = []

for i in range(n):
    tmp = list(map(int, input().split()))
    meeting.append(tmp)

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

print(meeting)

prev = meeting[0][1]
cnt = 1
for i in range(1, n):
    if meeting[i][0] >= prev:
        prev = meeting[i][1]
        cnt += 1

print(cnt)
