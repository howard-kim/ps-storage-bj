#Implementaion
def hansu(num):
    if num < 100:
        return True
    elif num == 1000:
        return False
    else:
        # arr = []
        # while num > 0:
        #     arr.append(num % 10)
        #     num //= 10
        a = num % 10
        num //= 10
        b = num % 10
        num //= 10
        c = num
        if b - a == c - b:
            return True
        else:
            return False
         


N = int(input())
ans = 0

#BruteForcing
for i in range(1, N + 1):
    if hansu(i) == True:
        ans += 1

print(ans)

