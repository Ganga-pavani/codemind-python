n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    if a.count(i)==i:
        if i not in x:
            x.append(i)
if x==[]:
    print(-1)
else:
    print('{:.2f}'.format(sum(x)/len(x)))