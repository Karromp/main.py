import random
from random import randint
lista= []
for i in range(4):
  tmp=[]
  for j in range(10):
    tmp.append(randint(1,9))
  lista.append(tmp)
print(lista)

import random

# Funkcja do tworzenia dwuwymiarowej listy losowych liczb całkowitych
def stworz_liste(wiersze, kolumny):
    lista = [[random.randint(1, 10) for _ in range(kolumny)] for _ in range(wiersze)]
    return lista

# Funkcja do sprawdzania sum wierszy i kolumn
def sprawdz_sumy(lista):
    for i in range(len(lista)):
        suma_wiersza = sum(lista[i])
        for j in range(len(lista[0])):
            suma_kolumny = sum(lista[k][j] for k in range(len(lista)))
            if suma_wiersza == suma_kolumny:
                return f"Wiersz: {i+1}, Kolumna: {j+1}"
    return "BRAK"

# Tworzenie i wyświetlanie listy dwuwymiarowej
wiersze = 4
kolumny = 4
lista_dwuwymiarowa = stworz_liste(wiersze, kolumny)
print("Lista dwuwymiarowa:")
for wiersz in lista_dwuwymiarowa:
    print(wiersz)

# Sprawdzanie sum wierszy i kolumn
wynik = sprawdz_sumy(lista_dwuwymiarowa)
print("Wynik sprawdzenia:")
print(wynik)
