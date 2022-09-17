s=input()
s=s.split(' ')
for i in s:
    a=max(i)
    b=min(i)
    print(abs(ord(a)-ord(b)),end=' ')