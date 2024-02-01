from collections import deque

y = [0, 1, 0, -1]
x = [1, 0, -1, 0]

graph = []
visited = [[0 for i in range(1005)]for u in range(1005)]
que = deque()

def possible(r, c):
    global N, M
    if r >= 0 and r < N and c >= 0 and c < M:
        return True
    return False

global N, M
M, N = map(int, input().split())
for i in range(N):
    graph.append(list(map(int, input().split())))
    for u in range(M):
        if graph[i][u] == 1:
            que.append([i, u])
            visited[i][u] = 1


while len(que) > 0:
    cur = que.popleft()

    # if graph[cur[0] - 1][cur[1]]
    # if graph[cur[0] + 1][cur[1]]
    # if graph[cur[0]][cur[1] - 1]
    # if graph[cur[0]][cur[1] + 1]
    for i in range(4):
        R = cur[0] + y[i]
        C = cur[1] + x[i]
        if possible(R, C) and graph[R][C] == 0 and visited[R][C] == 0:
            visited[R][C] = visited[cur[0]][cur[1]] + 1
            que.append([R, C])

# for i in range(N):
#     for u in range(M):
#         print(visited[i][u], end=' ')
#     print()

zero = 0
for i in range(N):
    for u in range(M):
        if visited[i][u] == 0 and graph[i][u] != -1:
            zero += 1

if zero > 0:
    print(-1)
else:
    print(max(map(max, visited)) - 1)



