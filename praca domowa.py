def funkcja(tekst,wzorzec):
    for i in range (0,len(tekst)-len(wzorzec)+1):
        if wzorzec[0]==tekst[i]:
            tmp=len(wzorzec)+i
            if wzorzec== tekst[i:tmp]:
                return true
