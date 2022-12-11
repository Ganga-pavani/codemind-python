s=input()
s=s.lower()
s=list(s)
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a.sort()
st='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'
for i in a:
    if i==' ':
        continue
    st+=i
print(st)