s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
s1=set(s1)
s2=set(s2)
a=[]
for i in s1:
    if i not in s2:
        if i!=' ':
            a.append(i)
for i in s2:
    if i not in s1:
        if i!=' ':
            a.append(i)
print(len(a))

