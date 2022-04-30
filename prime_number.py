n=int(input())
c=0
if n>1:
    for i in range(2,n,1):
        if n%i==0:
            c=1
            break
if c==0:
    print("prime")
else:
    print("not a prime")
    
