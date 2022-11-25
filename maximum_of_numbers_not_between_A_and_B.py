n=int(input())
li=list(map(int,input().split()))
a,b=map(int,input().split())
x=[]
for i in li:
    if i<a or i>b:
        x.append(i)
if x==[]:
    print(-1)
else:
    print(max(*x))