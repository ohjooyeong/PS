# 셔틀버스 프로그래머스

from collections import deque


def hourToMin(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])


def minToStr(time):
    hour = time // 60
    min = time % 60
    if hour < 10:
        hour = "0" + str(hour)
    hour = str(hour)

    if min < 10:
        min = "0" + str(min)
    min = str(min)
    return f"{hour}:{min}"


def solution(n, t, m, timetable):
    timetable = [hourToMin(time) for time in timetable]
    timetable.sort()
    timetable = deque(timetable)
    lastTime = 540 + (n - 1) * t  # 마지막 배차 시간

    for i in range(n):
        if len(timetable) < m:
            return minToStr(lastTime)
        if i == n - 1:
            if timetable[0] <= lastTime:
                lastTime = timetable[m - 1] - 1
            return minToStr(lastTime)
        cnt = 0
        for k in range(m):
            busTime = 540 + i * t
            if timetable and busTime >= timetable[k - cnt]:
                cnt += 1
                timetable.popleft()


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(
    solution(
        10,
        60,
        45,
        [
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
        ],
    )
)
