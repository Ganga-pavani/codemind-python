n=int(input())
temp=n
sum=0
prod=1
while temp!=0:
    prod=1
    r=temp%10
    for i in range(1,r+1):
        prod=prod*i
    sum=sum+prod
    temp=temp//10
if sum==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")