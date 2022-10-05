s=input()
c=0
for i in s:
    if s.count(i)>c:
        c=s.count(i)
for i in s:
    if s.count(i)<c:
        print(i)
        break
else:
    print(-1)