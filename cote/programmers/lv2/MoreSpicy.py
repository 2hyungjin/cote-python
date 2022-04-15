import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        last = heapq.heappop(scoville)
        if last >= K: break
        if len(scoville) < 1: return -1
        heapq.heappush(scoville, last + heapq.heappop(scoville) * 2)
        answer += 1
    return answer
