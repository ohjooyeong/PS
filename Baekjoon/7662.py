# 이중 우선순위 큐 7662
import heapq

T = int(input())


for i in range(T):
    n = int(input())

    max_heap = []
    min_heap = []

    for i in range(n):
        ope, num = input().split()
        num = int(num)
        if ope == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        else:
            if len(max_heap) == 0:
                pass
            elif num == 1:
                v = heapq.heappop(max_heap)[1]
                min_heap.remove(v)
            else:
                v = heapq.heappop(min_heap)
                max_heap.remove((-v, v))

    if min_heap:
        print(heapq.heappop(max_heap)[1], heapq.heappop(min_heap))
    else:
        print("EMPTY")

# 아직 실패한 코드 ㅠㅠ 시간초과 뜸
