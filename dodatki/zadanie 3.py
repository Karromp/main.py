from random import randint


def rzut(a):
    lista = []
    for i in range(a):
        lista.append(randint(1, 6))
    return lista



def kostka(i,wynik):

    wynik = 100
    if i == 1:
         return 1
    if i == 2 or 3:
        return wynik // 2
    if i == 4 or 5:
         return wynik * 2
    if i == 6:
         return wynik

def rezultat(wynik,lista):
    for i in lista:
        wynik=kostka(wynik,i)
     return wynik

print(rzut())

