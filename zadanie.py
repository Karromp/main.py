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
    return wynik
print(zadanie())
#gracz zaczyna ze 100 okt gra polega na 3 kolejnych rzutach koscia kazdy kolejny rzut zmienia ilosc pkt gracza wedlg wypadla 6 putnkty bez zmian wypada 4 5 pkt*2
#03 2 pkt /2 porzucamy czesc dziesientna wypada 1 gracz traci wszystkie pkt zostaje 1 napisz funkcje jednego erzutu koscia rzut napisz funkcie ktora a przyj,owac pkt