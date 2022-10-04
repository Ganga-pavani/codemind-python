n=int(input())
a=list(map(int,input().strip().split()))
b=[]
for i in a:
    if i not in b:
        if a.count(i)==1:
            b.append(i)
if not b:
    print('-1')
else:
    print(*b)