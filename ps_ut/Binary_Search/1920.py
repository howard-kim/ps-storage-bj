

N = int(input())
ln = list(map(int, input().split()))
ln.sort()
M = int(input())
lm = list(map(int, input().split()))

def bs(finder, nlist):

    left = 0
    right = len(nlist) - 1

    while left <= right:
        mid = (left + right) // 2

        if nlist[mid] == finder:
            return True
        elif nlist[mid] < finder:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def rec_bs(finder, left, right, nlist):
    if left > right:
        return False
    
    mid = (left + right) // 2
    if nlist[mid] == finder:
        return True
    elif nlist[mid] < finder:
        return rec_bs(finder, nlist[mid] + 1, right, nlist)
    else:
        return rec_bs(finder, left, nlist[mid] - 1, nlist)
    


for i in lm:
    if bs(i, ln) == True:
        print(1)
    else:
        print(0)
