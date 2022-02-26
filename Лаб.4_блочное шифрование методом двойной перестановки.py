import random
t=list(input('Исходный текст: '))
h=[]
a=[]
b=[]
x=0
i=0
l=len(t)%25
y=len(t)

while l<25:
    s=random.randint(97,122)
    t.append(chr(s))
    l+=1
l=0
q=len(t)/25

while x<q:
    while l<25:
        a.append(t[25*x+l])
        l+=1
    l=0
    
    while l<5:
        while i<5:
            b.append(a[l+5*i])
            i+=1
        i=0
        l+=1
    l=0
    a=[]
    
    while len(b)<49:
        s=random.randint(97,122)
        b.append(chr(s))
    
    while l<7:
        while i<7:
            h.append(b[l+7*i])
            i+=1
        i=0
        l+=1
    l=0
    b=[]
    x+=1
x=0
t=[]

print('Шифр:',''.join(map(str,h)))

while x<q:
    while l<49:
        a.append(h[49*x+l])
        l+=1
    l=0
    
    while l<7:
        while i<7:
            b.append(a[l+7*i])
            i+=1
        i=0
        l+=1
    l=0
    a=[]
    
    while i<25:
        a.append(b[i])
        i+=1
    i=0
    b=[]
    
    while l<5:
        while i<5:
            t.append(a[l+5*i])
            i+=1
        i=0
        l+=1
    a=[]
    l=0
    x+=1
h=[]

while i<y:
    h.append(t[i])
    i+=1
print('Дешифровка:',''.join(map(str,h)))
