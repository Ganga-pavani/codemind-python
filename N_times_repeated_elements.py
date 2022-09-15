n=int(input())
a=list(map(int,input().split()))
b=[]
z=int(input())
for i in a:
    if a.count(i)==z:
        if i not in b:
            b.append(i)
if b==[]:
    print("-1")
else:
    print(*b)