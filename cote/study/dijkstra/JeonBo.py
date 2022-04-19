import heapq

graph = None
distance = None
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

if __name__ == '__main__':
    N, M, C = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    distance = [1e9] * (N + 1)

    for i in range(M):
        X, Y, Z = map(int, input().split())
        graph[X].append((Y, Z))

    dijkstra(C)

    count=0
    max_distance=0

    for d in distance:
        if d!=1e9:
            count+=1
            max_distance = max(d,max_distance)

    print(count-1,max_distance)



