import random
a=list(input('Исходный текст:'))
print('Минимальный размер матрицы:',((len(a)**(1./2))//1)+1)
b=[]
c=[]
d=[]
x=[]
v=[]
z=[]
m=int(input('Размер первой матрицы:'))
n=int(input('Размер второй матрицы:'))
i=int(0)
l=int(0)
y=int(len(a))

while len(a)<m*m:
    s=random.randint(97, 122)
    a.append(chr(s))
u=int(len(a))

while l<m:
    while i<m:
        b.append(a[l+m*i])
        i+=1
    i=0
    l+=1
print('Шифр:',''.join(map(str, b)))
l=0

while len(b)<n*n:
    s=random.randint(97, 122)
    b.append(chr(s))

while l<n:
    while i<n:
        d.append(b[l+n*i])
        i+=1
    i=0
    l+=1
print('Шифр2:',''.join(map(str, d)))
l=0

while l<n:
    while i<n:
        x.append(d[l+n*i])
        i+=1
    i=0
    l+=1
l=0

while i<u:
    v.append(x[i])
    i+=1
print('Дешифровка1:',''.join(map(str, v)))
i=0

while l<m:
    while i<m:
        c.append(v[l+m*i])
        i+=1
    i=0
    l+=1
    
while i<y:
    z.append(c[i])
    i+=1
print('Дешифровка2:',''.join(map(str, z)))