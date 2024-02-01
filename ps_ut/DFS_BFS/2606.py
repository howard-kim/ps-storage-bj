from collections import deque


ans = 0

N = int(input())
M = int(input())
graph = [[0 for i in range(0, N+5)] for u in range(0, N+5)]
visited = [0 for i in range(0, N+5)]

for i in range(0, M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


queue = deque()

queue.append(1)
visited[1] = 1

while len(queue) > 0:
    cur = queue.popleft()
    for i in range(1, N + 1):
        if graph[cur][i] == 1 and visited[i] == 0:
            queue.append(i)
            ans += 1
            visited[i] = 1

print(ans)
 