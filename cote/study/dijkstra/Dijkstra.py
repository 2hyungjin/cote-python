graph = None
visited = None
distance = None


def get_smallest():
    min_value = 1e9
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            index = i
            min_value = distance[i]
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True


    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: distance[j[0]] = cost


if __name__ == '__main__':
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [1e9] * (n + 1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dijkstra(start)

    for i in range(1,n+1):
        if distance[i]==1e9:print("INF")
        else : print(distance[i])
