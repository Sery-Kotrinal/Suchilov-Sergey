a=list(input('Исходный текст:'))
k=list(input('Код:'))
j=[]
g=[]
f=[]
u=[]
v=[]
l=int(2)
p=int(0)

for i, q in enumerate(a, start=0):
    g.append(bin(ord(a[i])))
print('Биты:',g)

for i, q in enumerate(k, start=0):
    j.append(bin(ord(k[i])))
print('Биты:',j)

for i, q in enumerate(g, start=0):
    c=list(g[i])
    o=list(j[p])
    d=[]
    while l<9:
        if c[l]==o[l]:
            d.append(0)
        else:
            d.append(1)
        l+=1
    f.append(''.join(map(str, d)))
    l=2
    i+=1
    p+=1
    if p==len(j):
        p=0
i=0
l=0
print('Зашифрованные биты:',f)

for i, q in enumerate(f, start=0):
    c=list(f[i])
    o=list(j[p])
    del(o[0])
    del(o[0])
    d=[]
    while l<7:
        if c[l]==o[l]:
            d.append(0)
        else:
            d.append(1)
        l+=1
    l=0
    i+=1
    p+=1
    if p==len(j):
        p=0
    z=(''.join(map(str, d)))
    u.append(z)
    v.append(chr(int(z,2)))
print('Дешифрованные биты:',u)
print('Дешифрованный текст:',''.join(map(str, v)))