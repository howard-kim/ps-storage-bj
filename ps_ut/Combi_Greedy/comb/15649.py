from itertools import permutations

N, M = map(int, input().split())

nums = []

for num in range(1, N+1):
    nums.append(num)

perm = permutations(nums,M)

for result in perm:
    for n in result:
        print(n, end=" ")
    print()

