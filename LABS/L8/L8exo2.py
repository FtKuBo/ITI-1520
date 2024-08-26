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



