n=int(input())
li=list(map(int,input().split()))
b=[]
for i in li:
    if i not in b:
        b.append(i)
for j in b:
    print(j,li.count(j),end=" ")