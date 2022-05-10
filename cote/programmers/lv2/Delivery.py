import heapq


def solution(N, road, K):
    roads = [1e9] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    q = []

    for r in road:
        graph[r[1]].append((r[0], r[2]))
        graph[r[0]].append((r[1], r[2]))

    roads[1] = 0

    heapq.heappush(q, (1, 0))

    while q:
        now, dist = heapq.heappop(q)
        for i, c in graph[now]:
            cost = dist + c
            roads[i] = min(cost, roads[i])
            if roads[i] == cost:
                heapq.heappush(q, (i, roads[i]))

    print(roads)

    return len(list(filter(lambda a: a <= K, roads)))