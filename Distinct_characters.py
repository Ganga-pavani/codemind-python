s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a.sort()
x=''
for i in a:
    if i==' ':
        continue
    x+=i
print(x)