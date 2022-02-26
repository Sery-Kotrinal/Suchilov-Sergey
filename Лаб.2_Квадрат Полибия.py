import random
from random import randint
m=[]
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
x=int(0)
y=0
while y<100:
    x=randint(30,130)
    if x in m:
        x=randint(30,130)
    else:
        m.append(x)
        y+=1
y=0
while y<10:
    a.append(chr(m[y*10]))
    b.append(chr(m[y*10+1]))
    c.append(chr(m[y*10+2]))
    d.append(chr(m[y*10+3]))
    e.append(chr(m[y*10+4]))
    f.append(chr(m[y*10+5]))
    g.append(chr(m[y*10+6]))
    h.append(chr(m[y*10+7]))
    i.append(chr(m[y*10+8]))
    j.append(chr(m[y*10+9]))
    y+=1
y=0
print('Программа поддерживает только лаинский алфавит:')
s=list(input('Введите тект:'))
m=[]
while y<len(s):
    if s[y] in a:
        m.append(b[a.index(s[y])])
    if s[y] in b:
        m.append(c[b.index(s[y])])
    if s[y] in c:
        m.append(d[c.index(s[y])])
    if s[y] in d:
        m.append(e[d.index(s[y])])
    if s[y] in e:
        m.append(f[e.index(s[y])])
    if s[y] in f:
        m.append(g[f.index(s[y])])
    if s[y] in g:
        m.append(h[g.index(s[y])])
    if s[y] in h:
        m.append(i[h.index(s[y])])
    if s[y] in i:
        m.append(j[i.index(s[y])])
    if s[y] in j:
        m.append(a[j.index(s[y])])
    y+=1
y=0
print('Шифр:',''.join(map(str, b)))
n=str()
while y<len(m):
    if m[y] in a:
        n+=j[a.index(m[y])]
    if m[y] in b:
        n+=a[b.index(m[y])]
    if m[y] in c:
        n+=b[c.index(m[y])]
    if m[y] in d:
        n+=c[d.index(m[y])]
    if m[y] in e:
        n+=d[e.index(m[y])]
    if m[y] in f:
        n+=e[f.index(m[y])]
    if m[y] in g:
        n+=f[g.index(m[y])]
    if m[y] in h:
        n+=g[h.index(m[y])]
    if m[y] in i:
        n+=h[i.index(m[y])]
    if m[y] in j:
        n+=i[j.index(m[y])]
    y+=1
print('Дешифровка:',n)
