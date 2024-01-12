#napisz program ktory wczyta tekst oraz napisany literami łacińskimi nastepnie wyszuka wzorzec w tekscie
#w progeamie utworz funkcje znajdz
tekst="pdkopkpkopk"
wzorzec="pk"
def znajdz (tekst,wzorzec):
    dlugosc_tekstu=len(tekst)
    dlugosc_wzorca=len(wzorzec)
    for i in  range (dlugosc_tekstu-dlugosc_wzorca+1):
        if tekst[i:i+dlugosc_wzorca]==wzorzec:
            return True
    return False
wynik=znajdz(tekst, wzorzec)
if wynik:
    print ("wzorzec '{wzorzec}' wystepuje w tekscie")
else:
    print("wzorzec '{wzorzec}'nie  wystepuje w tekscie")

def znajdz(w, t):
    dw = len(w)
    dt = len(t)
    p = 0
    while p <= dt - dw:
        i = 0
        while i<dw and w[i]==t[p+i]:
            i+=1
        if i == dw:
            return p
        else:
            p+=1
    return -1
lista=[99,97,98,102]
suma=0
for i in lista:
        suma= suma + lista[0]
print(suma)

for i in lista:
    suma=suma-lista[0]