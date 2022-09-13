n=int(input())
li=list(map(int,input().split()))
b=[]
for i in li:
    if i not in b:
        b.append(i)
print(*b)