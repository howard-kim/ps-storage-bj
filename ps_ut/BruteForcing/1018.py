def paintCnt(chess):
    cnt1 = 0
    cnt2 = 0

    standard = 'W'
    for i in range(8):
        for j in range(8):
            if(chess[i][j] != standard):
                cnt1 += 1
            if(standard == 'W'):
                standard = 'B'
            else:
                standard = 'W'
        if(standard == 'W'):
            standard = 'B'
        else:
            standard = 'W'
    
    standard = 'B'
    for i in range(8):
        for j in range(8):
            if(chess[i][j] != standard):
                cnt2 += 1
            if(standard == 'W'):
                standard = 'B'
            else:
                standard = 'W'
        if(standard == 'W'):
            standard = 'B'
        else:
            standard = 'W'

    return min(cnt1,cnt2)

N, M = map(int, input().split())
inputCards = []

for i in range(N):
    row = input()
    inputCards.append(row)

ans = N*M

for i in range(0, N-8+1):
    for j in range(0, M-8+1):
        chess = []
        for a in range(8):
            line = []
            for b in range(8):
                line.append(inputCards[i+a][j+b])
            chess.append(line)
        if(paintCnt(chess)<ans):ans = paintCnt(chess)

print(ans)


        # row = inputCards[i,j]
    # chess.append(row)

# print(chess)

# N, M = map(int, input().split())
# original = []
# count = []

# for _ in range(N):
#     original.append(input())

# for a in range(N-7):
#     for b in range(M-7):
#         index1 = 0
#         index2 = 0
#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         index1 += 1
#                     if original[i][j] != 'B':
#                         index2 += 1
#                 else:
#                     if original[i][j] != 'B':
#                         index1 += 1
#                     if original[i][j] != 'W':
#                         index2 += 1
#         count.append(min(index1, index2))

# print(min(count))