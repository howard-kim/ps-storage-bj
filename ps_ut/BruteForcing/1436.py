def devil(n):
    six = 0
    numString = str(n)
    for i in numString:
        if(i == '6'):
            six += 1
            if(six >= 3):
                return True
        else:
            six = 0
    return False

N = int(input())
num = 0
cnt = 0
while(1):
    if (devil(num)):
       cnt += 1
       if(cnt == N):
           break
    num += 1
print(num)


# n = int(input())
# nth = 666
# count = 0

# while True:
#     if '666' in str(nth):   #1 n번째 수에 '666'이 포함되어 있다면(str이 아니면 무조건 1의자리부터 시작하니까)
#         count+=1               #2 카운트를 올려라
#     if count == n:          #4 카운트랑 n번째 수가 같다면 
#         print(nth)           #5 nth를 출력하고
#         break               #6 while문을 종료해라
#     nth+=1 