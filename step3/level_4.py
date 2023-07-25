total = int(input())
amount = int(input())
comp = 0
for i in range(amount) :
    price, entity = map(int, input().split())
    comp += price * entity

if(total == comp):
    print("Yes")
else:
    print("No")