from collections import deque

graph = [[] for i in range(1005)]
visited = [0 for i in range(1005)]

global V, N
N, M, V = map(int, input().split())

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(cur):
    global N
    visited[cur] = 1
    print(cur, end=' ')
    for i in graph[cur]:
        if visited[i] == 0:
            dfs(i)
    # for i in range(N + 1):
    #     if graph[cur][i] == 1 and visited[i] == 0:
    #         dfs(i)

def bfs():
    global V, N
    que = deque()
    visited[V] = 1
    print(V, end=' ')
    que.append(V)

    while len(que) > 0:
        cur = que.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                visited[i] = 1
                print(i, end=' ')
                que.append(i)
        # for i in range(N + 1):
        #     if graph[cur][i] == 1 and visited[i] == 0:
        #         visited[i] = 1
        #         print(i, end=' ')
        #         que.append(i)

dfs(V)
print()
visited = [0 for i in range(1005)]
bfs()