h, m = map(int, input().split())
if(m>=45):
    print("{:d} {:d}".format(h, m-45))
elif(h==0):
    print("{:d} {:d}".format(23, 15+m))
else :
    print("{:d} {:d}".format(h-1, 15+m))