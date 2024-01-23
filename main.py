# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
def func():
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
telefon={"edmund":123654234,"zuzia":987786543,"adam":567934008}
#for imie in telefon
a=(1,2,3,0)
print(a)
print(sorted(a))
a=0.3333333333333333*3
print(a)
from random import randint

print("Zgadywanie liczb z przedziału [0; 100]")
szukana = randint(0,100)
proba = 1
liczba = 0

while liczba != szukana:
    print("\nPróba ", proba, ": ", end="")
    liczba = int(input())
    if liczba < szukana:
        print("Za mała")
    else:
        if liczba > szukana:
            print("Za duża")
        else:
            print("Brawo! Udało ci się za", proba, "razem")
    proba = proba + 1
    #dana jest 2wymiarowa tablica o rozmiarze o2x04 o wartosciach 