
lista=[]
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
#w pliku liczby txt w oddzielnych wierszach znajduje sie 100 roznych liczb o dlugosci od 2 do 9 cyfr napisz funkcje lub program ktory da odpowiedz na ponizsze pytanie. Czynnikiem pierwszym danej liczby naturalnej zlozona jest dowolna liczba pierwsza ktora dzieli te liczbe calkowicie podaj ile jest w pliku liczb txt liczb w ktorych rozkladzie na cczynniki pierwsze wystepuje dokladnie 3 rozne czynniki, czynniki moga sie poiwtarzac z ktorych kazdy jest nieparzysty