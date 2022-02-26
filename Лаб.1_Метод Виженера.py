print('Программа работает только с латинским алфавитом')
t=str(input('Исходный текст:'))
k=list(input('Ключ:'))
c=str()
r=str()
m=[]
n=[]
l=[]
s=int(0)

for i, q in enumerate(k, start=1):
    l.append(ord(q)-96)

for i, q in enumerate(t, start=1):
    m.append(ord(q))
for i, q in enumerate(m, start=1):
    if s==len(k):
    	s-=len(k)
    h=int(l[s])
    a=q+h
    if a>122:
    	a-=26
    c+=chr(a)
    s+=1
print('Шифр:',c)
s=int(0)

for i, q in enumerate(c, start=1):
    n.append(ord(q))

for i, q in enumerate(n, start=1):
    if s==len(k):
    	s-=len(k)
    h=int(l[s])
    a=q-h
    if a<97:
    	if a!=32:
        	a+=26
    r+=chr(a)
    s+=1
print('Дешифровка:',r)