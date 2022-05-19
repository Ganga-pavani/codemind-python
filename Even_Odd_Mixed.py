n=int(input())
even=0
odd=0
while n>0:
    d=n%10
    n=n//10
    if d%2==0:
        even+=1
    else:
        odd+=1
if even>0 and odd==0:
    print("Even")
elif even==0 and odd>0:
    print("Odd")
else:
    print("Mixed")
    