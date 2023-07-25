h, m = map(int, input().split())
min = int(input())
hour = min // 60
min = min % 60
#print(h,m,hour,min)
m = m+min
h = h+hour
if(m>=60) :
    m = m-60
    h+=1
if(h >= 24):
    h = h%24

print("{:.0f} {:.0f}".format(h, m))