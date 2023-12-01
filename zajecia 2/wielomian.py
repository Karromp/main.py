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