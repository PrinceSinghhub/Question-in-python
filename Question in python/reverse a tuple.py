a=(1,2,3,5,"codex",6,9,10,90)
b=len(a)
c=[]
for i in range (1,b):
    d=a[-i]
    c.append(d)
c.append(a[0])
d=tuple(c)
print(d)

x=(1,2,3,4,5)
y=reversed(x)
print(tuple(y))