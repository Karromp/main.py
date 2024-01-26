w="kolorado"
szyfrogram=("")
m=8
k=3
klucz=[1,2,0]
#for i in range(k):
    #klucz.append(a)
    #a=a+1
    #
k=len(klucz)
def szyfruj(n):
    if n+k-1<m:
        for i in range(1,k):
            s=s+w[n+klucz[i-1]-1]
            szyfruj(n)
    else:
        while n<=m:
            if n<m:
                s=s+w[n-1]+w[n]
                n=n+2
            else:
                s=s+w[n-1]
                n=n+1
print (szyfruj(n))

#funkcja szyfruj(n)
#    jeżeli n+k-1<m
 #       dla i=1,2,3,…,k wykonuj
  #          s ← s+w[n+klucz[i]-1]
   #     szyfruj(n+k)
   # w przeciwnym razie
    #    dopóki n<=m
     #       jeżeli n<m
      #          s ← s+w[n+1]+w[n]
       #         n ← n+2
       #     w przeciwnym razie
       #         s ← s+w[n]
      #          n ← n+1