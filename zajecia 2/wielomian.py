x=3
listarg=[3,2,1,-1,-2]
s=4
def wielo(x,lista):
    listarg.reverse()
    w=1
    wielomian=listarg[0]
    print(wielomian)
    for i in range(1,s+1):
        w*= x
        wielomian+=w*listarg[i]
    return wielomian
def bintodec (s):
    p=len(s)-1
    w=0
    for i in s:
        if i=='1':
            w=w+2**p
        p-=1
    return w
