x=int(input())
a=list(map(int,input().split()))
y=int(input())
b=list(map(int,input().split()))
z=int(input())
c=0
for i in range(0,x):
    if z>=a[i] and z<=b[i]:
        c=c+1
print(c)