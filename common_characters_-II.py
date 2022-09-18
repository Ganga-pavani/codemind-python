s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
a=[]
for i in s1:
    if i in s2:
        if i!=' ':
            a.append(i)
print(len(set(a)))