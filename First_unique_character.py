s=input()
a=0
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if i!=j:
            if s[i]==s[j]:
                c+=1
    if c==0:
        print(s[i])
        a=1
        break
if a==0:
    print("-1")