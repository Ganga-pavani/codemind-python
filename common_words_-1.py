a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split(' ')
b=b.split(' ')
c=0
for i in a:
    if i in b:
        c+=1
print(c)