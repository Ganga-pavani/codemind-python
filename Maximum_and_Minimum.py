n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    if a.count(i)==i:
        x.append(i)
if x==[]:
    print(-1)
else:
    print(min(*x),end=" ")
    print(max(*x))