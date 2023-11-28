def bintofloat(n,ilebit=0):
    wynik=0
    for i in range(2,ilebit+2):
        if n[i]=='1'or n[i]=='0':
            if n[i]=='1':
                wynik+=2**(-i+1)
        else:
            return"ERROR"
    return wynik
print(bintofloat(0,1))
