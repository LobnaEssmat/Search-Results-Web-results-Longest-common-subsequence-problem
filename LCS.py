##m is responsible for column length (length of first string )
##n is responsible for row length (length of second string )
##We'll iterate row by row

def lcs(X, Y):
    m=len(X)
    n=len(Y)
    L = [[0 for x in range(m+1)] for y in range(n+1)] 
 
    for i in range(1,n+1,1):
        for j in range(1,m+1,1):
            if X[j-1] == Y[i-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print(L[n][m])

    LCS =""
    i = n
    j = m
    while i > 0 and j > 0:
        up = L[i-1][j]
        left = L[i][j-1]
        if  X[j-1]==Y[i-1]:
            LCS=Y[i-1]+LCS
            i-=1
            j-=1

        elif L[i][j] == up:
            i-=1
        else:
            j-=1

    print (LCS)
 
# Driver program
X = "AGGTAB"
Y = "GXTXAYB"
lcs(X, Y)
