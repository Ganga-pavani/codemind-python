n=int(input())
sum=0
a=0
x=n*n
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
z=sum*sum
while z>0:
    d=z%10
    a=a*10+d
    z=z//10
if x==a:
    print("True")
else:
    print("False")
    