def transpose(L):
    mt=[[0]*len(L) for i in range(len(L[0]))]
    for y in range(len(L)):
        for i in range(len(L[0])):
            mt[i][y]=L[y][i]
    return mt

print(transpose([[1,2,3],[4,5,6]]))













