n=int(input())
a=list(map(int,input().split()))
c=1000
for i in a:
    i=abs(i)
    i=str(i)
    if len(i)<c:
        c=len(i)
r=0
for i in a:
    i=abs(i)
    i=str(i)
    if len(i)==c:
        r+=1
print(r)