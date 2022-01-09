# 야근지수 12927
import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    ans = 0

    heap = []
    for w in works:
        heapq.heappush(heap, -w)

    while n != 0:
        num = heapq.heappop(heap)
        heapq.heappush(heap, num + 1)
        n -= 1

    for w in heap:
        ans += w ** 2
    return ans


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
