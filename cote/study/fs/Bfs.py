from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9


def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    while queue:
        v = (queue.popleft())
        print(v, end=' ')
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node]=True


if __name__ == '__main__':
    bfs(graph, 1, visited)
