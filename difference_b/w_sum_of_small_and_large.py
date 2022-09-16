s=input()
s=s.split(' ')
a=0
b=0
for i in s:
    a=a+ord(max(i))
    b=b+ord(min(i))
print(abs(a-b))
