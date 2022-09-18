s=input()
t=[]
r=s.lower()
for i in r:
    if i not in t:
        if i!=' ':
            t.append(i)
print(len(t))