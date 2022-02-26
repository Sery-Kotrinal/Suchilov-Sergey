import random
a=list(input('Исходный текст:'))
print('Минимальный размер матрицы:',((len(a)**(1./2))//1)+1)
b=[]
c=[]
z=[]
m=int(input('Размер матрицы:'))
i=int(0)
l=int(0)
y=int(len(a))

while len(a)<m*m:
    s=random.randint(97, 122)
    a.append(chr(s))

while l<m:
    while i<m:
        b.append(a[l+m*i])
        i+=1
    i=0
    l+=1
print('Шифр:',''.join(map(str, b)))
l=0

while l<m:
    while i<m:
        c.append(b[l+m*i])
        i+=1
    i=0
    l+=1
while i<y:
    z.append(c[i])
    i+=1
print('Дешифровка:',''.join(map(str, z)))