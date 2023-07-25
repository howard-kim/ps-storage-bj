import sys
while True:
    a, b = map(int, sys.stdin.readline().rsplit())
    if(a==0 and b==0): break
    sys.stdout.write("{:d}\n".format(a+b))
    