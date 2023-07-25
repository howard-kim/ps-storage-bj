import sys
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().rsplit())
    sys.stdout.write("Case #{:d}: {:d} + {:d} = {:d}\n".format(i+1,a,b,a+b))