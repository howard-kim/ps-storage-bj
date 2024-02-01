# x = [1, 0, -1, 0]
# y = [0, 1, 0, -1]

# global N, M
# N, M = map(int, input().split())
# graph = []
# visited = [[0 for i in range(105)] for u in range(105)]

# for i in range(N):
#     graph.append([int(n) for n in str(input())])

# print(graph)

# def possible(r, c):
#     global N, M
#     if r>=0 and r<N and c>=0 and c<M:
#         return True
#     return False


# def dfs(cur, mov, cnt):
#     # print("this is ",cnt)
#     # cnt +=1
#     print(cur)
    
#     global N,M
#     if(cur[0] == N-1 and cur[1] == M-1):
#         print(mov)
        
#     for i in range(4):
#         R = cur[0] + y[i]
#         C = cur[1] + x[i]
#         for i in range(4):
#             nextR = R + y[i]
#             nextC = C = x[i]
#             if(possible(R,C) and graph[R][C]==1 and visited[R][C] ==0,possible(nextR,nextC) and graph[nextR][nextC]==1 and visited[nextR][nextC] ==0):
#                 visited[R][C] = 1
#                 mov+=1
#                 # print(mov)
#                 dfs([R,C],mov,cnt)
        
        
# dfs([0,0], 1, 1)


#     # visited[cur] = 1
#     # for i in graph[cur]:
#     #     if visited[i] == 0:
#     #         mov+=1
#     #         dfs(i,mov)
from collections import deque

x = [1, 0, -1, 0]
y = [0, 1, 0, -1]

global N, M
N, M = map(int, input().split())
graph = []
visited = [[0 for i in range(105)] for u in range(105)]
que = deque()

for i in range(N):
    graph.append([int(n) for n in str(input())])

que.append([0,0])
visited[0][0] = 1

def possible(r,c):
    global N, M
    if r>=0 and r<N and c>=0 and c<M:
        return True
    return False

def bfs():
    global N, M
    mov = 1
    while len(que) > 0:
        cur = que.popleft()
        for i in range(4):
            R = cur[0] + y[i]
            C = cur[1] + x[i]
            if(possible(R,C) and graph[R][C] == 1 and visited[R][C] == 0):
                visited[R][C] = visited[cur[0]][cur[1]]+1
                que.append([R,C])

bfs()
print(visited[N-1][M-1])