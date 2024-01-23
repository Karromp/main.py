
lista=[]from math import sqrt

# pobieranie danych z pliku txt
def pobieraniezpliku(filename):
    liczby = []
    with open(filename, "r") as file:
        for i in file:
            liczby.append(int(i))
    return liczby


def czynnikipierwsze(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1

    return czynniki


res = pobieraniezpliku("liczby.txt")


def spr(liczba):
    czynnikinieparzyste = []
    for i in czynnikipierwsze(liczba):
        if i % 2 != 0:
            if i not in czynnikinieparzyste:
                czynnikinieparzyste.append(i)
        else:
            return False
    if len(czynnikinieparzyste) == 3:
        return True
    else:
        return False


ile = 0
for n in res:
    if spr(n):
        ile += 1
print(ile)
with open("pilotka.txt","r") as file:
    for j in file:
        lista.append(j.strip())
print(lista)

def func(a,k):
    for i in range(len(a)-k):
        if a[i]>a[i+k]:
            return False
    return True
for i in range(2,100):
    if func(lista,i):
        print(i)
