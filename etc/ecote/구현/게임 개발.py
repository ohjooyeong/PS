n, m = map(int, input().split())
x, y, direction = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

direct = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + direct[direction][0]
    ny = y + direct[direction][1]

    if visited[nx][ny] == 0 and maps[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - direct[direction][0]
        ny = y - direct[direction][1]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
