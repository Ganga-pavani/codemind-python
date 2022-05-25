a=int(input())
b=int(input())
for i in range(a,b+1):
    sum=0
    temp=i
    while temp!=0:
        r=temp%10
        sum=sum*10+r
        temp=temp//10
    if(i==sum):
        print(i,end=" ")
    
