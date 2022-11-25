n=int(input())
li=list(map(int,input().split()))
x=[]
for i in li:
    if li.count(i)==i:
        if i not in x:
            x.append(i)
print(len(x))