t=str(input('Исходный текст:'))
k=list(input('Ключ:'))
c=str()
r=str()
m=[]
n=[]
s=int(0)

for i, q in enumerate(t, start=1):
    m.append(ord(q))

for i, q in enumerate(m, start=1):
    if s==len(k):
    	s-=len(k)
    h=int(k[s])
    c+=chr(q+h)
    s+=1
print('Шифр:',c)

for i, q in enumerate(c, start=1):
    n.append(ord(q))

for i, q in enumerate(n, start=1):
    if s==len(k):
    	s-=len(k)
    h=int(k[s])
    r+=chr(q-h)
    s+=1
print('Дешифровка:',r)