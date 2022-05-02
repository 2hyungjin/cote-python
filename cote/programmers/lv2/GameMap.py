from collections import deque

def solution(maps):
    nx = [1,-1,0,0]
    ny = [0,0,1,-1]

    n, m = len(maps[0]),len(maps)

    visited = [[-1] * n for _ in range(m)]

    deq = deque()

    deq.append([0,0])

    visited[0][0]=1

    while deq:
        y,x = deq.popleft()

        if x== n-1 and y==m-1 : break

        for i in range(4):
            _x,_y = x+nx[i], y+ny[i]
            if 0<=_x<n and 0<=_y<m and visited[_y][_x]==-1 and maps[_y][_x]==1:
                visited[_y][_x]=visited[y][x]+1
                deq.append([_y,_x])

    return visited[-1][-1]