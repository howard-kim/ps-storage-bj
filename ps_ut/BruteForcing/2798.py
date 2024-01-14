# from itertools import combinations



# def MaxUnderM(target, numbers):
#     MUM = 0
#     min_difference = 1000000000000

#     for number in numbers:
#         if number <= target:
#             difference = target - number
#             if difference == 0:
#                 return number
#             elif difference < min_difference:
#                 MUM = number
#     return MUM            
    

# def sumOfThree(nums):
#     sum = 0
#     for i in range(3):
#         sum += int(nums[i])
#     return sum

# line1 = input()
# NandM = line1.split()
# N = NandM[0]
# M = int(NandM[1])

# line2 = input()
# cards_num = line2.split()
# cards = []
# combiSums = []

# for i in range (0, int(N)):
#     cards.append(cards_num[i])

# # for i in cards:
# #     print(i)

# combi = list(combinations(cards,3))

# for i in range(0, len(combi)):
#     combiSums.append(sumOfThree(combi[i]))

# print(MaxUnderM(M, combiSums))

# print(combi[0])
# print(combiSums[0])


# for i in combi:



# def nCr(n, ans, r):
#     if n == len(nums):
#         if len(ans) == r:
#             temp = [i for i in ans]
#             answer_list.append(temp)
#         return
#     ans.append(nums[n])
#     nCr(n + 1, ans, r)
#     ans.pop()
#     nCr(n + 1, ans, r)

# nCr(0, [], 3)
# print(answer_list)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] > M:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])

print(result)


