n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    count=0
    k=a[i]
    for j in range(1,k+1):
        if a[i]==j*j:
            count=1
            break
    if count==1:
        sum=sum+a[i]
print(sum)