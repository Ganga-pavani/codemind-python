n=int(input())
temp=n
rev=0
r=0
k=0
if n<0:
    n=n*(-1)
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp<0:
    k=rev*-1
    print(k)
else:
    print(rev)