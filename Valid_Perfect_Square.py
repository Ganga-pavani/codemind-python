t=int(input())
while t>0:
    n=int(input())
    x=0
    for i in range(1,n+1):
        if n==i*i:
            x=1
    if x==1:
        print("True")
    else:
        print("False")
    t=t-1