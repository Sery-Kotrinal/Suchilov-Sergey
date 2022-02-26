print('Программа работает только с латинским алфавитом')
t=str(input('Исходный текст:'))
k=list('hkzksTtsgsgjxfuhtslhtuscgx')
j=list('jyhrzathqwhkdkhytudkH')
c=str()
r=str()
m=[]
n=[]
l=[]
w=[]
s=int(0)

for i, q in enumerate(k, start=1):
    l.append(ord(q)-64)
    
for i, q in enumerate(j, start=1):
    w.append(ord(q)-64)

for i, q in enumerate(t, start=1):
    m.append(ord(q))
    
for i, q in enumerate(m, start=1):
    if s==len(k):
    	s-=len(k)
    h=int(l[s])
    if q==32:
        a=q
    else:
        a=q+h
        if a>122:
            if q!=32:
                a-=58
    c+=chr(a)
    s+=1
print('Шифр:',c)
s=int(0)
m=[]

for i, q in enumerate(c, start=1):
    n.append(ord(q))

for i, q in enumerate(n, start=1):
    if s==len(j):
    	s-=len(j)
    h=int(w[s])
    a=q+h
    if a>122:
        a-=58
    r+=chr(a)
    s+=1
c=str()
print('Шифр2:',r)
s=int(0)
n=[]

for i, q in enumerate(r, start=1):
    m.append(ord(q))

for i, q in enumerate(m, start=1):
    if s==len(j):
    	s-=len(j)
    h=int(w[s])
    a=q-h
    if a<65:
    	if a!=32:
    		a+=58
    c+=chr(a)
    s+=1
r=str()
print('Дешифровка:',c)
s=int(0)

for i, q in enumerate(c, start=1):
    n.append(ord(q))

for i, q in enumerate(n, start=1):
    if s==len(k):
    	s-=len(k)
    h=int(l[s])
    if q==32:
        a=q
    else:
        a=q-h
        if a<65:
        	a+=58
    r+=chr(a)
    s+=1
print('Дешифровка2:',r)