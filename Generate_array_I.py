n=int(input())
li=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    for j in range(0,li[i+1]):
        b.append(li[i])
print(*b)
    