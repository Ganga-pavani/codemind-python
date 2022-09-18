s=input()
a=s.lower()
c=0
for i in a:
    if a.count(i)==1:
        if i!=' ':
            c+=1
print(c)