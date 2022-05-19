n=int(input())
arr=list(map(int,input().split()))
even=0
odd=0
for i in range(0,n):
    if arr[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print(even,end=" ")
print(odd,end=" ")