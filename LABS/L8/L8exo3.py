def transpose(L):
    mt=[[0]*len(L) for i in range(len(L[0]))]
    for y in range(len(L)):
        for i in range(len(L[0])):
            mt[i][y]=L[y][i]
    return mt

print(transpose([[1,2,3],[4,5,6]]))


###################################

def somme_matrices(m,n):
    for i in range(len(m)):
        for y in range(len(m[i])):
            m[i][y]+=n[i][y]
    return m

print(somme_matrices([[1,2],[3,4]],[[1,1],[1,1]]))


###################################

def produit_matrices(a,b):
    i=0
    c=[]
    while  i < len(a):
        j=0
        c.append([])
        while j<len(b[0]):
            k=0
            c[i].append(0)
            while k< len(a[0]):
                c[i][j] += a[i][k] * b[k][j]
                k+=1
            j+=1
        i+=1
    return c

print(produit_matrices([[1,2,3],[4,5,6]],[[1,2],[3,4],[5,6]]))
