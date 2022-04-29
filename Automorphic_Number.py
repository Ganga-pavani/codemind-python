num=int(input())
n=len(str(num))
sq=num**2
x=sq%pow(10,n)
if(x==num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
