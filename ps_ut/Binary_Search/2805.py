# N, M = map(int, input().split())
# trees = list(map(int, input().split()))
# trees.sort()

# cut = trees[len(trees)-1]
# take = 0

# while(1):
#     trees.sort()
#     for i in trees:
#         if(i>cut):
#             i-=1
#             take+=1
#     if(take>=M):
#         break
#     cut -= 1


# print(cut)

N, M = map(int, input().split()) 
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while(start<=end):
    take = 0
    mid = (start+end)//2
    cut = mid
    for tree in trees:
        if(tree>cut):
            take += tree - cut
    
    if(take >= M):
        start = mid + 1
    else:
        end = mid - 1

print(end)


