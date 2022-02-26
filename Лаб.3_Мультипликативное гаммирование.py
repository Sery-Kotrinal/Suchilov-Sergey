a=5
m=4096
Y0=m-5
z=[]
Y=(Y0*a)%m
x=0
z.append(Y)

while x<4096:
    y=(Y0*a)%m
    z.append(Y)
    Y0=Y
    x+=1
x=0

t=list(input('Введите тект:'))
j=[]

while x<len(t):
    r=int(ord(t[x]))
    e=z[x]
    c=r^e
    j.append(c)
    x+=1
x=0

print('Шифр:',''.join(map(str,j)))
f=str()
o=[]

while x<len(t):
    o.append(chr(j[x]^z[x]))
    f+=(chr(j[x]^z[x]))
    x+=1
print('Дешифровка:',f)
