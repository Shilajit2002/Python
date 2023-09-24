n=int(input())

flag=False
if n<0:
    flag=True
    n*=(-1)

result=0
remainder=0
while n>0:
    remainder=n%10
    result=result*10+remainder
    n//=10

if flag:
    result*=-1

print(result)
