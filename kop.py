#Dana jest funkcja Kop opisana poniżej:
#
#Funkcja Kop(A, n, m, i, j):
  #  1. Jeżeli i > n lub j > m, to:
   #     2. Zwróć 0
    #3. k1 := Kop(A, n, m, i + 1, j)
 #   4. k2 := Kop(A, n, m, i, j + 1)
  #  5. Jeżeli k1 > k2, to:
   #     6. Zwróć A[i][j] + k1
   # 7. w przeciwnym przypadku:
   #     8. Zwróć A[i][j] + k2
#Dana jest dwuwymiarowa tablica 𝐴[0..2][0..4]=[[4,2,1,10,5],[0,4,22,2,8],[40,1,1,1,1]],
#oraz 𝑛=3 i 𝑚=5. Podaj wyniki działania funkcji Kop dla określonych wartości 𝑖 oraz 𝑗. a. i = 1 j = 3 b. i = 1 j = 1 c. i = 0 j = 0






def Kop(A,n,m,i,j):
    if i>n :
        return 0
    if j>m:
        return 0
    k1 = Kop(A, n, m, i + 1, j)
    k2 = Kop(A, n, m, i, j + 1)
    if k1 > k2:
        return A[i][j]+k1
    else:
        return A[i][j]+k2


𝐴=[[4,2,1,10,5],[0,4,22,2,8],[40,1,1,1,1]]
𝑛=2
𝑚=4
i=1
j=5
print(Kop(A,n,m,i,j ))

