n=int(input())
x=0
y=0
for i in range(1,n+1):
    if n%i==0:
        x=x+1
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    n=n//10
for i in range(1,rev+1):
    if rev%i==0:
        y=y+1
if x==2 and y==2:
    print("circular prime")
elif x==2:
    print("prime but not a circular prime")
else:
    print("not prime")
    