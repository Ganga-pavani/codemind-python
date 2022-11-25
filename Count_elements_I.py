a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
c=[]
for i in m:
    if i in n:
        if i not in c:
            c.append(i)
print(len(c))