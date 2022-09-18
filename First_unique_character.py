s=input()
s=s.lower()
b=[]
for i in s:
    b.append(i)
for i in s:
    if b.count(i)==1:
        print(i)
        break
else:
    print(-1)