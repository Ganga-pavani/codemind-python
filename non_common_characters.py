s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
a=[]
for i in s1:
    if i not in s2:
        a.append(i)
for j in s2:
    if j not in s1:
        a.append(j)
a=set(a)
a=list(a)
a.sort()
for i in a:
    if i!=' ':
        print(i,end='')
