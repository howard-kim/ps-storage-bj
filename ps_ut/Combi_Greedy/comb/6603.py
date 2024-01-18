from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    k = nums[0]
    if k == 0:
        break

    nums = nums[1:]
    comb = combinations(nums, 6)

    for printer in comb:
        for i in printer:
            print(i, end=' ')
        print()
    print()


