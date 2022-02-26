a=list(input('Исходный текст:'))
g=[]
f=[]
u=[]
v=[]
l=int(2)

for i, q in enumerate(a, start=0):
    g.append(bin(ord(a[i])))
print('Биты:',g)

for i, q in enumerate(g, start=0):
    c=list(g[i])
    d=[]
    while l<9:
        if c[l]=='1':
            d.append(0)
        else:
            d.append(1)
        l+=1
    f.append(''.join(map(str, d)))
    l=2
    i+=1
i=0
l=0
print('Зашифрованные биты:',f)

for i, q in enumerate(f, start=0):
    c=list(f[i])
    d=[]
    while l<7:
        if c[l]=='1':
            d.append(0)
        else:
            d.append(1)
        l+=1
    l=0
    i+=1
    z=(''.join(map(str, d)))
    u.append(z)
    v.append(chr(int(z,2)))
print('Дешифрованные биты:',u)
print('Дешифрованный текст:',''.join(map(str, v)))