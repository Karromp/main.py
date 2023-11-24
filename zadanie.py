def silnia(n):
    w=1
    for i in range (1,n+1):
        w*=i
    return w
def zadanie():
    eps=0.00001
    wynik=1.0
    k=3
    znak= -1
    skladnik=1/silnia(k)
    while skladnik>=eps:
        wynik+= znak * skladnik
        k+=2
        skladnik=1/silnia(k)
        znak-=znak