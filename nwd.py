
a = int(input("Podaj liczbę a:"))
b = int(input("Podaj liczbę b:"))

print("NWD(", a, ",", b, ")=", end="")
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)
# Najwiekszy wspolny dzielnik
# Logowanie się do sysytemy określoną ilość razy

a = int(input("Podaj liczbę a:"))
b = int(input("Podaj liczbę b:"))
login_baza = "admin"
haslo_baza = "1234admin4321"

print("NWD(",a,",",b,")=",end="")
while a != b:
    if a > b:
        a = a -b
zalogowano = False
i = 1
while i <= 3 and zalogowano == False:
    login = input("Login: ")
    haslo = input("Hasło: ")
    if login == login_baza and haslo == haslo_baza:
        print("Logowanie prawidłowe")
        zalogowano = True
    else:
        b = b - a
print(a)
        print("Błąd logowania! Pozostało ", 3-i, " prób")
        i = i + 1
