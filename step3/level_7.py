import sys
t = int(input())
for i in range(t):
    a, b = map(int,sys.stdin.readline().rsplit())
    print("Case #{:d}: {:d}".format(i+1,a+b))